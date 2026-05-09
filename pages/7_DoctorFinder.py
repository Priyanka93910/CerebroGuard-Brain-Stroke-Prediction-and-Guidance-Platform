import streamlit as st
import urllib.parse
import urllib.request
import json
import math
import sqlite3
from datetime import datetime, date, timedelta
import sys
sys.path.append('..')

# ─────────────────────────────────────────────────────────────
# DATABASE HELPERS
# Uses a SEPARATE table 'walk_in_appointments' to avoid
# conflict with the existing slot-based 'appointments' table.
# ─────────────────────────────────────────────────────────────
DB = "cerebroguard.db"

def _conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def ensure_walkin_table():
    """Create walk_in_appointments table if it doesn't exist."""
    con = _conn()
    con.execute("""
    CREATE TABLE IF NOT EXISTS walk_in_appointments (
        walkin_id       INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id         INTEGER NOT NULL,
        username        TEXT NOT NULL,
        hospital_name   TEXT NOT NULL,
        hospital_addr   TEXT,
        hospital_lat    REAL,
        hospital_lon    REAL,
        appt_date       TEXT NOT NULL,
        appt_time       TEXT NOT NULL,
        reason          TEXT,
        status          TEXT DEFAULT 'Confirmed',
        booked_at       TEXT DEFAULT CURRENT_TIMESTAMP
    )""")
    con.commit()
    con.close()

def book_walkin(user_id, username, hosp_name, hosp_addr,
                h_lat, h_lon, appt_date, appt_time, reason):
    ensure_walkin_table()
    con = _conn()
    con.execute("""
        INSERT INTO walk_in_appointments
        (user_id, username, hospital_name, hospital_addr,
         hospital_lat, hospital_lon, appt_date, appt_time, reason)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (user_id, username, hosp_name, hosp_addr,
          h_lat, h_lon, str(appt_date), appt_time, reason))
    con.commit()
    con.close()

def get_walkin_appointments(user_id):
    ensure_walkin_table()
    con = _conn()
    rows = con.execute("""
        SELECT * FROM walk_in_appointments
        WHERE user_id=?
        ORDER BY appt_date DESC, appt_time DESC
    """, (user_id,)).fetchall()
    con.close()
    return [dict(r) for r in rows]

def cancel_walkin(walkin_id):
    con = _conn()
    con.execute(
        "UPDATE walk_in_appointments SET status='Cancelled' WHERE walkin_id=?",
        (walkin_id,))
    con.commit()
    con.close()

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Find Doctors - CerebroGuard",
    page_icon="🏥", layout="wide")

st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
    }
    .block-container { padding-top: 1.5rem !important; }

    .page-title {
        text-align: center; color: #1b5e20;
        font-size: 40px; font-weight: 800; margin-bottom: 4px;
    }
    .emergency-banner {
        background: linear-gradient(135deg, #f44336, #e91e63);
        color: white; padding: 16px; border-radius: 14px;
        text-align: center; font-size: 17px; font-weight: 700;
        margin: 14px 0 20px 0;
    }
    .hosp-card {
        background: white; border: 2px solid #c8e6c9;
        border-radius: 16px; padding: 20px 22px;
        margin-bottom: 4px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.07);
        transition: transform .2s;
    }
    .hosp-card:hover { transform: translateY(-3px); }
    .hosp-title { color: #1b5e20; font-size: 18px; font-weight: 800; margin-bottom: 4px; }
    .hosp-type  { color: #4caf50; font-size: 14px; font-weight: 600; margin-bottom: 8px; }
    .hosp-info  { color: #555;    font-size: 14px; line-height: 1.85; }
    .map-btn {
        display: inline-block; text-decoration: none !important;
        border-radius: 22px; font-size: 13px; font-weight: 700;
        padding: 8px 16px; margin: 6px 4px 10px 0;
        transition: transform .2s;
    }
    .map-btn:hover { transform: translateY(-2px); }
    .btn-dir  { background: linear-gradient(135deg,#1a73e8,#0d47a1); color: white !important; }
    .btn-view { background: linear-gradient(135deg,#34a853,#0d652d); color: white !important; }
    .gmaps-cta {
        display: inline-block; text-decoration: none !important;
        background: linear-gradient(135deg, #1a73e8, #0d47a1);
        color: white !important; font-size: 15px; font-weight: 800;
        padding: 12px 28px; border-radius: 30px;
        box-shadow: 0 5px 18px rgba(26,115,232,.35);
        transition: all .3s;
    }
    .gmaps-cta:hover { transform: translateY(-2px); }
    .appt-confirmed {
        background: #e8f5e9; border-left: 5px solid #4caf50;
        border-radius: 12px; padding: 16px 20px; margin-bottom: 10px;
    }
    .appt-cancelled {
        background: #fce4ec; border-left: 5px solid #e91e63;
        border-radius: 12px; padding: 16px 20px; margin-bottom: 10px; opacity: .8;
    }
    .overpass-note {
        background: #e3f2fd; border-left: 4px solid #1565c0;
        border-radius: 8px; padding: 10px 16px;
        color: #0d47a1; font-size: 13px; margin: 8px 0 16px 0;
    }
    .divider { border: none; border-top: 2px solid #c8e6c9; margin: 24px 0; }
    .stButton > button {
        background: linear-gradient(135deg, #4caf50, #66bb6a) !important;
        color: white !important; border: none !important;
        border-radius: 10px !important; font-weight: 700 !important;
    }
    div[data-testid="stTabs"] button {
        font-size: 16px !important; font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# GEO / OVERPASS HELPERS
# ─────────────────────────────────────────────────────────────
def geocode(loc):
    """Convert location string to lat/lon using Nominatim."""
    try:
        url = ("https://nominatim.openstreetmap.org/search?q="
               + urllib.parse.quote(loc)
               + "&format=json&limit=1&addressdetails=1")
        req = urllib.request.Request(
            url, headers={"User-Agent": "CerebroGuard/2.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode())
        if data:
            return (float(data[0]["lat"]),
                    float(data[0]["lon"]),
                    data[0].get("display_name", loc))
    except Exception as e:
        st.warning(f"Geocoding error: {e}")
    return None, None, None

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2
         + math.cos(math.radians(lat1))
         * math.cos(math.radians(lat2))
         * math.sin(dlon/2)**2)
    return round(R * 2 * math.asin(math.sqrt(a)), 2)

def fetch_hospitals(lat, lon, radius=8000):
    """
    Fetch hospitals near lat/lon from OpenStreetMap.
    Returns ONLY hospitals relevant to neurology / stroke / neurosurgery.
    Uses strict keyword matching — excludes diabetes, general, eye, dental etc.
    """

    # ── STRICT neuro-relevant keywords (hospital name must contain one of these)
    NEURO_KEYWORDS = [
        # Direct neuro terms
        "neuro", "brain", "stroke", "spine", "spinal", "cranio",
        # Top hospital chains known for neurology
        "apollo", "yashoda", "kims", "nims", "continental",
        "medicover", "sunshine", "manipal", "fortis", "max hospital",
        "aiims", "aster", "columbia", "narayana", "sakra",
        "gleneagles", "care hospital", "omega hospital",
        # Known neuro-centre naming patterns
        "neuroscience", "neuro care", "neuro centre", "neuro center",
        "stroke centre", "stroke center",
        "institute of neurology", "neurology institute",
        "brain and spine", "spine and brain",
    ]

    # ── EXCLUDE keywords — hospitals that clearly aren't neuro-relevant ────────
    EXCLUDE_KEYWORDS = [
        "diabetes", "diabetic", "eye", "dental", "teeth", "skin",
        "fertility", "ivf", "maternity", "women", "child", "paedia",
        "pediatric", "ortho", "kidney", "renal", "cancer", "oncol",
        "cardiac", "heart", "lung", "pulmo", "gastro", "liver",
        "ent", "ear nose", "plastic", "cosmet", "hair", "ayurved",
        "homeo", "veterinary", "animal", "pharmacy", "nursing home",
        "blood bank", "covid", "tb hospital", "chest",
    ]

    # ── Overpass query — only hospitals (not clinics/pharmacies) ─────────────
    q = (
        "[out:json][timeout:30];"
        "(node[\"amenity\"=\"hospital\"](around:{r},{la},{lo});"
        "node[\"healthcare\"=\"hospital\"](around:{r},{la},{lo});"
        "way[\"amenity\"=\"hospital\"](around:{r},{la},{lo});"
        "way[\"healthcare\"=\"hospital\"](around:{r},{la},{lo});"
        "relation[\"amenity\"=\"hospital\"](around:{r},{la},{lo}););"
        "out center 50;"
    ).format(r=radius, la=lat, lo=lon)

    try:
        url  = "https://overpass-api.de/api/interpreter"
        data = urllib.parse.urlencode({"data": q}).encode()
        req  = urllib.request.Request(url, data=data, headers={
            "User-Agent": "CerebroGuard/2.0",
            "Content-Type": "application/x-www-form-urlencoded"})
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.loads(r.read().decode())

        all_hospitals = []
        for el in res.get("elements", []):
            tags = el.get("tags", {})
            name = tags.get("name") or tags.get("name:en")
            if not name:
                continue
            if el["type"] == "node":
                hlat, hlon = el["lat"], el["lon"]
            else:
                ctr = el.get("center", {})
                hlat = ctr.get("lat", lat)
                hlon = ctr.get("lon", lon)
            all_hospitals.append({
                "name":    name,
                "lat":     hlat,
                "lon":     hlon,
                "type":    "Neurology Hospital",
                "phone":   tags.get("phone") or tags.get("contact:phone") or "",
                "website": tags.get("website") or tags.get("contact:website") or "",
                "addr":    tags.get("addr:full") or tags.get("addr:street") or "",
                "dist":    haversine(lat, lon, hlat, hlon),
                "specialty": tags.get("healthcare:speciality", ""),
            })

        def is_neuro(h):
            name_lower = h["name"].lower()
            # Must NOT match any exclude keyword
            if any(ex in name_lower for ex in EXCLUDE_KEYWORDS):
                return False
            # Must match at least one neuro keyword
            return any(kw in name_lower for kw in NEURO_KEYWORDS)

        def is_multispeciality(h):
            name_lower = h["name"].lower()
            if any(ex in name_lower for ex in EXCLUDE_KEYWORDS):
                return False
            multi_kw = [
                "super specialit", "superspecialit",
                "multispecialit", "multi specialit",
                "multi-specialit", "speciality hospital",
                "specialty hospital",
            ]
            return any(kw in name_lower for kw in multi_kw)

        # ── Priority 1: strict neuro keyword match ────────────────────────────
        neuro_hospitals = [h for h in all_hospitals if is_neuro(h)]

        # ── Priority 2: multispeciality hospitals (have neuro depts) ──────────
        if len(neuro_hospitals) < 3:
            multi = [h for h in all_hospitals
                     if is_multispeciality(h) and h not in neuro_hospitals]
            neuro_hospitals = neuro_hospitals + multi

        # ── Priority 3: fallback — all hospitals (user's area may be small) ───
        if not neuro_hospitals:
            neuro_hospitals = [
                h for h in all_hospitals
                if not any(ex in h["name"].lower() for ex in EXCLUDE_KEYWORDS)
            ]

        neuro_hospitals.sort(key=lambda x: x["dist"])
        return neuro_hospitals[:15]

    except Exception as e:
        st.warning(f"Could not fetch hospital data: {e}")
        return []

def build_leaflet(lat, lon, display_name, hospitals):
    """Build a self-contained Leaflet.js HTML map."""
    hj   = json.dumps(hospitals)
    dn60 = display_name[:60].replace("\\", "").replace("'", "").replace('"', "")
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
      integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV/XN/WLHs=" crossorigin=""></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: 100%; height: 100%; overflow: hidden; background: #e8f5e9; }}
  #map {{ width: 100%; height: 100%; border-radius: 12px; }}
  @keyframes pulse {{
    0%   {{ box-shadow: 0 0 0 0 rgba(76,175,80,0.7); }}
    70%  {{ box-shadow: 0 0 0 12px rgba(76,175,80,0); }}
    100% {{ box-shadow: 0 0 0 0 rgba(76,175,80,0); }}
  }}
  .loading {{
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    font-family: sans-serif; font-size: 16px; color: #1b5e20;
    background: white; padding: 20px 30px; border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  }}
</style>
</head>
<body>
<div id="loading" class="loading">🗺️ Loading map...</div>
<div id="map"></div>
<script>
// Wait for Leaflet to load
window.addEventListener('load', function() {{
  document.getElementById('loading').style.display = 'none';

  var map = L.map('map', {{
    zoomControl: true,
    scrollWheelZoom: true,
    attributionControl: true
  }}).setView([{lat}, {lon}], 14);

  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19,
    subdomains: 'abc'
  }}).addTo(map);

  // ── Your location marker ──────────────────────────────────
  var youIcon = L.divIcon({{
    className: '',
    html: '<div style="background:#dc3545;width:20px;height:20px;border-radius:50%;'
        + 'border:3px solid white;box-shadow:0 3px 10px rgba(0,0,0,0.4);"></div>',
    iconSize: [26, 26], iconAnchor: [13, 13]
  }});
  L.marker([{lat}, {lon}], {{icon: youIcon}})
   .addTo(map)
   .bindPopup('<b style="color:#dc3545;font-size:14px;">📍 Your Location</b><br>'
            + '<small style="color:#555;">{dn60}</small>')
   .openPopup();

  // ── 5 km search radius ────────────────────────────────────
  L.circle([{lat}, {lon}], {{
    color: '#dc3545', fillColor: '#dc3545',
    fillOpacity: 0.05, weight: 1.5,
    radius: 5000, dashArray: '6,4'
  }}).addTo(map).bindTooltip('5 km search radius', {{
    permanent: false, direction: 'top'
  }});

  // ── Hospital icon ─────────────────────────────────────────
  var hospIcon = L.divIcon({{
    className: '',
    html: '<div style="background:#4caf50;width:34px;height:34px;border-radius:50%;'
        + 'border:3px solid white;display:flex;align-items:center;justify-content:center;'
        + 'font-size:17px;box-shadow:0 3px 10px rgba(0,0,0,0.3);'
        + 'animation:pulse 2s infinite;">🏥</div>',
    iconSize: [40, 40], iconAnchor: [20, 20]
  }});

  // ── Plot hospitals ────────────────────────────────────────
  var hospitals = {hj};
  hospitals.forEach(function(h) {{
    var addr  = h.addr  ? '<br>📍 ' + h.addr  : '';
    var phone = h.phone ? '<br>📞 <a href="tel:' + h.phone + '" style="color:#4caf50;">'
                        + h.phone + '</a>' : '';
    var popup = '<div style="min-width:220px;font-family:sans-serif;line-height:1.6;">'
      + '<div style="color:#1b5e20;font-size:15px;font-weight:700;margin-bottom:6px;">🏥 ' + h.name + '</div>'
      + '<div style="color:#555;font-size:13px;">'
      + '🩺 ' + h.type
      + addr + phone
      + '<br>📏 <b>' + h.dist + ' km away</b>'
      + '</div>'
      + '<div style="margin-top:10px;display:flex;gap:6px;">'
      + '<a href="' + h.dir  + '" target="_blank" style="flex:1;text-align:center;padding:7px 10px;'
      + 'background:#1a73e8;color:white;border-radius:18px;text-decoration:none;'
      + 'font-size:12px;font-weight:700;">🧭 Directions</a>'
      + '<a href="' + h.view + '" target="_blank" style="flex:1;text-align:center;padding:7px 10px;'
      + 'background:#34a853;color:white;border-radius:18px;text-decoration:none;'
      + 'font-size:12px;font-weight:700;">🗺 Maps</a>'
      + '</div></div>';

    var marker = L.marker([h.lat, h.lon], {{icon: hospIcon}}).addTo(map);
    marker.bindPopup(popup, {{maxWidth: 280, autoPan: true}});
    marker.on('mouseover', function() {{ this.openPopup(); }});
    marker.on('click',     function() {{ this.openPopup(); }});
  }});

  // ── Legend ────────────────────────────────────────────────
  var legend = L.control({{position: 'bottomright'}});
  legend.onAdd = function() {{
    var d = L.DomUtil.create('div');
    d.innerHTML =
      '<div style="background:white;padding:10px 14px;border-radius:10px;'
    + 'box-shadow:0 2px 8px rgba(0,0,0,0.2);font-size:13px;line-height:2;">'
    + '<b style="display:block;margin-bottom:4px;">Legend</b>'
    + '<span style="display:inline-block;width:12px;height:12px;background:#4caf50;'
    + 'border-radius:50%;vertical-align:middle;margin-right:6px;"></span>Hospital/Clinic<br>'
    + '<span style="display:inline-block;width:12px;height:12px;background:#dc3545;'
    + 'border-radius:50%;vertical-align:middle;margin-right:6px;"></span>Your Location'
    + '</div>';
    return d;
  }};
  legend.addTo(map);

  // Force map to recalculate size after iframe loads
  setTimeout(function() {{ map.invalidateSize(); }}, 300);
}});
</script>
</body>
</html>"""

# ─────────────────────────────────────────────────────────────
# SESSION STATE DEFAULTS
# ─────────────────────────────────────────────────────────────
for key, default in [
    ("booking_hospital", None),
    ("hospitals_list",   []),
    ("searched_lat",     None),
    ("searched_lon",     None),
    ("searched_loc",     ""),
    ("searched_display", ""),
    ("df_active_tab",    0),       # 0=Search, 1=Book, 2=MyAppts
    ("df_pending_book",  None),    # hospital set by Book button
]:
    if key not in st.session_state:
        st.session_state[key] = default

logged_in = st.session_state.get("logged_in", False)
user_id   = st.session_state.get("user_id",   None)
username  = st.session_state.get("username",  "Guest")

# ─────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────
st.markdown(
    "<h1 class='page-title'>🏥 Find Neurologists Near You</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<div class='emergency-banner'>"
    "🚨 EMERGENCY? Call <b>108</b> (India Ambulance) immediately!"
    "</div>",
    unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# Process pending Book button click (must be before tabs render)
# ─────────────────────────────────────────────────────────────
if st.session_state.df_pending_book:
    st.session_state.booking_hospital = st.session_state.df_pending_book
    st.session_state.df_pending_book  = None

# ─────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────
tab_search, tab_book, tab_my = st.tabs(
    ["🔍 Search Hospitals", "📅 Book Appointment", "📋 My Appointments"])

# ══════════════════════════════════════════════════════════════
# TAB 1 — SEARCH
# ══════════════════════════════════════════════════════════════
with tab_search:
    c1, c2 = st.columns([4, 1])
    with c1:
        user_location = st.text_input(
            "loc", label_visibility="collapsed",
            placeholder="Enter city / area  e.g. Gajuwaka Vizag, Banjara Hills Hyderabad, Mumbai",
            value=st.session_state.searched_loc,
            key="location_input")
    with c2:
        search_clicked = st.button("🔍 Search", use_container_width=True)

    # ── Trigger search when button clicked ───────────────────
    if search_clicked and user_location.strip():
        with st.spinner(f"📡 Locating '{user_location}'…"):
            lat, lon, display_name = geocode(user_location.strip())

        if not lat:
            st.error(
                f"❌ Could not find **{user_location}**. "
                "Try a more specific name, e.g. 'Gajuwaka Vizag' or 'Banjara Hills Hyderabad'.")
        else:
            # ✅ Save to session so results persist across reruns
            st.session_state.searched_lat     = lat
            st.session_state.searched_lon     = lon
            st.session_state.searched_display = display_name
            st.session_state.searched_loc     = user_location.strip()

            with st.spinner("🔎 Loading nearby hospitals from OpenStreetMap…"):
                hospitals = fetch_hospitals(lat, lon)
            st.session_state.hospitals_list = hospitals

    # ── Display results if we have a searched location ────────
    lat          = st.session_state.searched_lat
    lon          = st.session_state.searched_lon
    display_name = st.session_state.searched_display
    hospitals    = st.session_state.hospitals_list
    loc_label    = st.session_state.searched_loc

    if lat and lon:
        st.success(f"📍 Showing results for: **{display_name}**")

        # ── Google Maps "Open in Google Maps" button ──────────
        gmaps_url = (
            "https://www.google.com/maps/search/neurologist+stroke+specialist+near+"
            + urllib.parse.quote(loc_label)
            + f"/@{lat},{lon},14z")
        st.markdown(
            "<div style='text-align:center;margin:10px 0 18px 0'>"
            f"<a href='{gmaps_url}' target='_blank' class='gmaps-cta'>"
            f"🧠 Find Neurologists Near &quot;{loc_label}&quot; on Google Maps"
            "</a></div>",
            unsafe_allow_html=True)

        # ── Leaflet map ───────────────────────────────────────
        st.markdown("### 🗺️ Interactive Map")

        # Build hospital list with direction/view links for JS
        hosp_for_map = []
        for h in hospitals:
            hosp_for_map.append({
                "name":  h["name"],
                "lat":   h["lat"],
                "lon":   h["lon"],
                "type":  h["type"],
                "phone": h["phone"],
                "addr":  h["addr"],
                "dist":  h["dist"],
                "dir":   (f"https://www.google.com/maps/dir/?api=1"
                          f"&destination={h['lat']},{h['lon']}"),
                "view":  ("https://www.google.com/maps/search/"
                          + urllib.parse.quote(h["name"])
                          + f"/@{h['lat']},{h['lon']},17z"),
            })

        st.markdown(
            "<div class='overpass-note'>"
            "🧠 Showing <b>neurology & stroke hospitals</b> near your location · "
            "Click pins to get Google Maps directions"
            "</div>",
            unsafe_allow_html=True)

        # ── Map: Google Maps Embed — neurologist specific ─────────────────────
        gmap_embed_query = urllib.parse.quote(f"neurology hospital stroke specialist near {loc_label}")
        gmap_embed_url = (
            f"https://maps.google.com/maps?q={gmap_embed_query}"
            f"&t=m&z=14&ie=UTF8&iwloc=&output=embed"
        )
        st.markdown(
            f'<div style="width:100%;height:500px;border-radius:14px;overflow:hidden;'
            f'border:2px solid #c8e6c9;box-shadow:0 4px 16px rgba(0,0,0,0.12);'
            f'margin:8px 0 16px 0;">'
            f'<iframe src="{gmap_embed_url}" '
            f'width="100%" height="500" '
            f'style="border:0;display:block;" '
            f'allowfullscreen="" loading="lazy" '
            f'referrerpolicy="no-referrer-when-downgrade">'
            f'</iframe></div>',
            unsafe_allow_html=True)

        # Show individual hospital pins as clickable Google Maps links below map
        if hosp_for_map:
            st.markdown("#### 📍 Hospital Locations on Google Maps")
            pin_cols = st.columns(min(len(hosp_for_map[:6]), 3))
            for idx, h in enumerate(hosp_for_map[:6]):
                with pin_cols[idx % 3]:
                    gmaps_pin = (
                        "https://www.google.com/maps/search/"
                        + urllib.parse.quote(h["name"] + " " + loc_label)
                        + f"/@{h['lat']},{h['lon']},16z"
                    )
                    st.markdown(
                        f"<div style='background:white;border:1px solid #c8e6c9;"
                        f"border-radius:10px;padding:10px 12px;margin:4px 0;"
                        f"text-align:center;'>"
                        f"<div style='font-size:13px;font-weight:700;color:#1b5e20;"
                        f"margin-bottom:6px;'>🏥 {h['name'][:30]}</div>"
                        f"<div style='font-size:12px;color:#555;margin-bottom:8px;'>"
                        f"📏 {h['dist']} km away</div>"
                        f"<a href='{gmaps_pin}' target='_blank' "
                        f"style='background:#1a73e8;color:white;padding:5px 12px;"
                        f"border-radius:12px;text-decoration:none;font-size:12px;"
                        f"font-weight:700;'>🗺 View on Maps</a>"
                        f"</div>",
                        unsafe_allow_html=True)

        # ── Hospital cards ────────────────────────────────────
        st.markdown(
            f"### 🧠 Neurology & Stroke Hospitals Near **{loc_label}**")

        if not hospitals:
            st.info(
                "ℹ️ No neurology hospitals found within 8 km. "
                "Try the Google Maps buttons below to search directly.")
        else:
            st.caption(f"✅ {len(hospitals)} hospital(s) with neurology/stroke departments found")
            col_a, col_b = st.columns(2)
            for i, h in enumerate(hospitals[:10]):
                with (col_a if i % 2 == 0 else col_b):
                    addr_line  = f"<br>📍 {h['addr']}"  if h["addr"]  else ""
                    phone_line = f"<br>📞 {h['phone']}" if h["phone"] else ""
                    st.markdown(
                        "<div class='hosp-card'>"
                        f"<div class='hosp-title'>🏥 {h['name']}</div>"
                        f"<div class='hosp-type'>🧠 Neurology / Stroke Centre</div>"
                        f"<div class='hosp-info'>"
                        f"📏 <b>{h['dist']} km away</b>"
                        f"{addr_line}{phone_line}</div>"
                        "</div>",
                        unsafe_allow_html=True)

                    dir_url  = (f"https://www.google.com/maps/dir/?api=1"
                                f"&destination={h['lat']},{h['lon']}")
                    view_url = ("https://www.google.com/maps/search/"
                                + urllib.parse.quote(h["name"] + " neurology")
                                + f"/@{h['lat']},{h['lon']},17z")
                    st.markdown(
                        f"<a href='{dir_url}' target='_blank'"
                        f" class='map-btn btn-dir'>🧭 Directions</a>"
                        f"<a href='{view_url}' target='_blank'"
                        f" class='map-btn btn-view'>🗺 View on Maps</a>",
                        unsafe_allow_html=True)

                    if logged_in:
                        if st.button(
                                "📅 Book Appointment",
                                key=f"bk_{i}",
                                use_container_width=True):
                            # Store hospital and trigger rerun — Tab 2 reads it
                            st.session_state.df_pending_book = h
                            st.session_state.booking_hospital = h
                            st.rerun()
                    else:
                        st.markdown(
                            "<div style='font-size:13px;color:#888;margin:4px 0;'>"
                            "🔒 <a href='pages/2_Login.py' style='color:#4caf50;'>"
                            "Login</a> to book an appointment</div>",
                            unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)

        # ── Specialist shortcuts ──────────────────────────────
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("### 🔎 Search by Specialist Type")
        sc1, sc2, sc3, sc4 = st.columns(4)
        specs = [
            ("🧠 Neurologist",       "neurologist"),
            ("⚡ Stroke Specialist", "stroke+specialist+hospital"),
            ("🩺 Neurosurgeon",      "neurosurgeon"),
            ("🏥 Neuro Hospital",    "neurology+hospital"),
        ]
        for idx, (label, term) in enumerate(specs):
            surl = (
                f"https://www.google.com/maps/search/{term}+near+"
                + urllib.parse.quote(loc_label)
                + f"/@{lat},{lon},13z")
            [sc1, sc2, sc3, sc4][idx].markdown(
                f"<div style='text-align:center'>"
                f"<a href='{surl}' target='_blank' class='gmaps-cta'"
                f" style='font-size:13px;padding:9px 14px'>{label}</a>"
                f"</div>",
                unsafe_allow_html=True)
    else:
        st.markdown(
            "<div style='text-align:center;padding:50px 20px;color:#777'>"
            "<h3>🔍 Enter a location above to find hospitals near you</h3>"
            "<p>Real hospital data from OpenStreetMap · "
            "Interactive map · Google Maps directions</p>"
            "</div>",
            unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 2 — BOOK APPOINTMENT
# ══════════════════════════════════════════════════════════════
with tab_book:
    if not logged_in:
        st.warning("🔒 Please login to book an appointment.")
        if st.button("🔐 Go to Login", key="login_book"):
            st.switch_page("pages/2_Login.py")
        st.stop()

    st.markdown("### 📅 Book a Neurology Appointment")

    hospitals_for_select = st.session_state.hospitals_list

    if not hospitals_for_select:
        st.info(
            "ℹ️ Please search for hospitals in the **🔍 Search Hospitals** tab first, "
            "then come back here to book.")
    else:
        hosp_names = [h["name"] for h in hospitals_for_select]

        # ── Pre-select hospital clicked via Book button ───────────────────────
        preselect = 0
        bh = st.session_state.booking_hospital
        if bh and bh.get("name") in hosp_names:
            preselect = hosp_names.index(bh["name"])

        selected_name = st.selectbox(
            "🏥 Select Neurology Hospital",
            hosp_names, index=preselect,
            key="book_select")
        sel = next(h for h in hospitals_for_select if h["name"] == selected_name)

        # ── Update session when user changes dropdown ─────────────────────────
        st.session_state.booking_hospital = sel

        # ── Hospital info card ────────────────────────────────────────────────
        addr_bit  = f"<br>📍 {sel['addr']}"  if sel["addr"]  else ""
        phone_bit = f"<br>📞 {sel['phone']}" if sel["phone"] else ""
        dir_url   = f"https://www.google.com/maps/dir/?api=1&destination={sel['lat']},{sel['lon']}"
        st.markdown(
            "<div style='background:#e8f5e9;border-radius:14px;"
            "padding:18px 22px;margin:10px 0 20px 0;"
            "border-left:6px solid #4caf50;'>"
            f"<b style='color:#1b5e20;font-size:17px;'>🏥 {sel['name']}</b><br>"
            f"<span style='color:#2e7d32;font-size:13px;font-weight:600;'>"
            f"🧠 Neurology / Stroke Centre</span><br>"
            f"<span style='color:#555;font-size:14px;'>"
            f"📏 {sel['dist']} km away{addr_bit}{phone_bit}</span><br>"
            f"<a href='{dir_url}' target='_blank' "
            f"style='display:inline-block;margin-top:10px;padding:7px 16px;"
            f"background:#1a73e8;color:white;border-radius:16px;"
            f"text-decoration:none;font-size:13px;font-weight:700;'>"
            f"🧭 Get Directions to this Hospital</a>"
            f"</div>",
            unsafe_allow_html=True)

        # ── Date & Time ───────────────────────────────────────────────────────
        d_col, t_col = st.columns(2)
        with d_col:
            min_date  = date.today() + timedelta(days=1)
            appt_date = st.date_input(
                "📆 Appointment Date",
                min_value=min_date, value=min_date,
                key="appt_date_input")
        with t_col:
            time_slots = [
                "09:00 AM","09:30 AM","10:00 AM","10:30 AM",
                "11:00 AM","11:30 AM","12:00 PM","02:00 PM",
                "02:30 PM","03:00 PM","03:30 PM","04:00 PM",
                "04:30 PM","05:00 PM","05:30 PM","06:00 PM",
            ]
            appt_time = st.selectbox(
                "⏰ Preferred Time Slot",
                time_slots, key="appt_time_input")

        # ── Specialist preference ─────────────────────────────────────────────
        specialist = st.selectbox(
            "🩺 Specialist Required",
            ["Neurologist", "Stroke Specialist", "Neurosurgeon",
             "Neuro-Physician", "Rehabilitation Specialist", "Any Available"],
            key="specialist_input")

        reason = st.text_area(
            "📝 Reason / Symptoms (optional)",
            placeholder="e.g. Stroke risk detected, severe headache, weakness in limbs…",
            height=100, key="reason_input")

        # ── Summary card ──────────────────────────────────────────────────────
        st.markdown(
            "<div style='background:#f1f8e9;border-radius:12px;"
            "padding:14px 18px;margin:10px 0;border:1px solid #c8e6c9;'>"
            "<b style='color:#1b5e20;'>📋 Appointment Summary</b><br>"
            f"<span style='font-size:14px;color:#333;line-height:2;'>"
            f"🏥 <b>{sel['name']}</b><br>"
            f"📆 <b>{appt_date}</b> at <b>{appt_time}</b><br>"
            f"🩺 Specialist: <b>{specialist}</b>"
            f"</span></div>",
            unsafe_allow_html=True)

        if st.button("✅ Confirm Appointment", use_container_width=True):
            full_reason = f"[{specialist}] {reason}" if reason else specialist
            book_walkin(
                user_id=user_id,   username=username,
                hosp_name=sel["name"], hosp_addr=sel["addr"],
                h_lat=sel["lat"],      h_lon=sel["lon"],
                appt_date=appt_date,   appt_time=appt_time,
                reason=full_reason)
            st.success(
                f"🎉 Appointment confirmed at **{sel['name']}** "
                f"on **{appt_date}** at **{appt_time}**!")
            st.balloons()
            st.session_state.booking_hospital = None
            st.markdown(
                f"<a href='{dir_url}' target='_blank' class='gmaps-cta'"
                f" style='font-size:14px;padding:10px 22px;'>"
                f"🧭 Get Directions to {sel['name']}</a>",
                unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 3 — MY APPOINTMENTS
# ══════════════════════════════════════════════════════════════
with tab_my:
    if not logged_in:
        st.warning("🔒 Please login to view your appointments.")
        if st.button("🔐 Login Now", key="login_my"):
            st.switch_page("pages/2_Login.py")
        st.stop()

    st.markdown(f"### 📋 Appointments for **{username}**")
    appts = get_walkin_appointments(user_id)

    if not appts:
        st.info("📭 No appointments yet. Search for a hospital and book one!")
    else:
        confirmed_n = sum(1 for a in appts if a["status"] == "Confirmed")
        cancelled_n = sum(1 for a in appts if a["status"] == "Cancelled")
        st.markdown(
            f"<div style='color:#555;font-size:15px;margin-bottom:16px'>"
            f"<b style='color:#2e7d32'>{confirmed_n} Confirmed</b>"
            f" &nbsp;·&nbsp; "
            f"<b style='color:#880e4f'>{cancelled_n} Cancelled</b>"
            f"</div>",
            unsafe_allow_html=True)

        for a in appts:
            is_future = (
                datetime.strptime(a["appt_date"], "%Y-%m-%d").date()
                >= date.today())
            cls   = ("appt-confirmed"
                     if a["status"] == "Confirmed"
                     else "appt-cancelled")
            badge = ("✅ Confirmed"
                     if a["status"] == "Confirmed"
                     else "❌ Cancelled")
            bc    = ("#2e7d32"
                     if a["status"] == "Confirmed"
                     else "#880e4f")
            addr_row = (f"📍 <b>Address:</b> {a['hospital_addr']}<br>"
                        if a["hospital_addr"] else "")
            dir_url  = (f"https://www.google.com/maps/dir/?api=1"
                        f"&destination={a['hospital_lat']},{a['hospital_lon']}")
            view_url = ("https://www.google.com/maps/search/"
                        + urllib.parse.quote(a["hospital_name"])
                        + f"/@{a['hospital_lat']},{a['hospital_lon']},17z")

            st.markdown(
                f"<div class='{cls}'>"
                "<div style='display:flex;justify-content:space-between;"
                "align-items:center;margin-bottom:8px'>"
                f"<span style='font-size:17px;font-weight:800;color:#1b5e20'>"
                f"🏥 {a['hospital_name']}</span>"
                f"<span style='font-size:13px;font-weight:700;color:{bc}'>"
                f"{badge}</span></div>"
                "<div style='color:#555;font-size:14px;line-height:1.9'>"
                f"📆 <b>Date:</b> {a['appt_date']}"
                f" &nbsp;|&nbsp; ⏰ <b>Time:</b> {a['appt_time']}<br>"
                f"📝 <b>Reason:</b> {a['reason']}<br>"
                f"{addr_row}"
                f"🕒 <b>Booked:</b> {a['booked_at'][:16]}"
                "</div></div>",
                unsafe_allow_html=True)

            btn1, btn2, btn3 = st.columns([1.4, 1.4, 3])
            with btn1:
                st.markdown(
                    f"<a href='{dir_url}' target='_blank'"
                    f" class='map-btn btn-dir'>🧭 Directions</a>",
                    unsafe_allow_html=True)
            with btn2:
                st.markdown(
                    f"<a href='{view_url}' target='_blank'"
                    f" class='map-btn btn-view'>🗺 Maps</a>",
                    unsafe_allow_html=True)
            with btn3:
                if a["status"] == "Confirmed" and is_future:
                    if st.button(
                            "🚫 Cancel",
                            key=f"cancel_{a['walkin_id']}"):
                        cancel_walkin(a["walkin_id"])
                        st.success("Appointment cancelled.")
                        st.rerun()

            st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# NAVIGATION
# ─────────────────────────────────────────────────────────────
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
n1, n2, n3, n4, n5 = st.columns(5)
with n1:
    if st.button("🏠 Home",             use_container_width=True):
        st.switch_page("main.py")
with n2:
    if st.button("🧮 Predictor",        use_container_width=True):
        st.switch_page("pages/5_Predictor.py")
with n3:
    if st.button("💬 Health Assistant", use_container_width=True):
        st.switch_page("pages/6_Chatbot.py")
with n4:
    if st.button("📊 Dashboard",        use_container_width=True):
        st.switch_page("pages/9_Dashboard.py")
with n5:
    if st.button("📞 Contact",          use_container_width=True):
        st.switch_page("pages/4_Contact.py")

st.markdown("""
<div style='text-align:center;color:#1b5e20;padding:20px;'>
    © 2025 CerebroGuard | Doctor Appointment System
</div>""", unsafe_allow_html=True)