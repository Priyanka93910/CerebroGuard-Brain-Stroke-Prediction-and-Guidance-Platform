# Enhanced Knowledge Base for CerebroGuard Chatbot
# Import this in 6_Chatbot.py for extended responses

def get_enhanced_response(question):
    """
    Enhanced chatbot response system with comprehensive medical information
    """
    question_lower = question.lower()
    
    # Comprehensive response database
    knowledge_base = {
        # Stroke Basics
        "what is stroke": {
            "response": "A stroke occurs when blood supply to part of the brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. There are two main types: **Ischemic stroke** (87% of cases) - caused by blocked arteries, and **Hemorrhagic stroke** (13% of cases) - caused by bleeding in the brain. Brain cells begin to die within minutes, making immediate medical attention critical.",
            "related": ["symptoms", "types", "emergency"]
        },
        
        "ischemic stroke": {
            "response": "Ischemic stroke is the most common type (87% of strokes), caused by a blood clot blocking blood flow to the brain. Risk factors include atherosclerosis (plaque buildup), atrial fibrillation, and blood clotting disorders. Treatment includes clot-busting medications (tPA) if given within 3-4.5 hours, and mechanical thrombectomy for severe cases.",
            "related": ["treatment", "prevention"]
        },
        
        "hemorrhagic stroke": {
            "response": "Hemorrhagic stroke occurs when a blood vessel in the brain ruptures, causing bleeding. Causes include high blood pressure, aneurysms, arteriovenous malformations (AVMs), and blood thinners. It's less common but more deadly. Treatment may involve surgery to stop bleeding and relieve pressure on the brain.",
            "related": ["blood pressure", "emergency"]
        },
        
        # Symptoms & Warning Signs
        "symptoms": {
            "response": "**Common stroke symptoms** - Remember **F.A.S.T:**\n\n**F**ace drooping (one side droops or is numb)\n**A**rm weakness (one arm is weak or numb)\n**S**peech difficulty (slurred speech or trouble speaking)\n**T**ime to call emergency (call 108 immediately)\n\nOther symptoms: sudden confusion, trouble seeing, dizziness, loss of balance, severe headache with no known cause.",
            "related": ["emergency", "tia"]
        },
        
        "tia": {
            "response": "A Transient Ischemic Attack (TIA) or 'mini-stroke' has the same symptoms as a stroke but typically lasts only a few minutes and causes no permanent damage. However, **it's a serious warning sign** - 1 in 3 people who have a TIA will eventually have a stroke, with about half occurring within a year. Seek immediate medical attention even if symptoms resolve.",
            "related": ["symptoms", "prevention"]
        },
        
        # Emergency & Treatment
        "emergency": {
            "response": "**STROKE IS A MEDICAL EMERGENCY!** Call 108 immediately if you suspect stroke. **Time is brain** - every minute counts. For ischemic stroke, clot-busting drugs (tPA) must be given within 3-4.5 hours. Do NOT drive yourself. Note the time symptoms started. Do NOT eat or drink anything.",
            "related": ["symptoms", "treatment"]
        },
        
        "treatment": {
            "response": "Stroke treatment depends on type:\n\n**Ischemic Stroke:**\n- tPA (tissue plasminogen activator) within 3-4.5 hours\n- Mechanical thrombectomy within 24 hours\n- Antiplatelet drugs (aspirin)\n- Anticoagulants\n\n**Hemorrhagic Stroke:**\n- Surgery to relieve pressure\n- Coiling or clipping of aneurysms\n- Blood pressure control\n- Medications to reduce brain swelling",
            "related": ["recovery", "medication"]
        },
        
        # Prevention
        "prevention": {
            "response": "**Key prevention strategies:**\n\n1. **Control blood pressure** (<120/80 mmHg)\n2. **Maintain healthy weight** (BMI 18.5-24.9)\n3. **Exercise regularly** (150 min/week)\n4. **Eat healthy diet** (Mediterranean or DASH diet)\n5. **Don't smoke** or quit if you do\n6. **Limit alcohol** (1 drink/day for women, 2 for men)\n7. **Manage diabetes** (HbA1c <7%)\n8. **Control cholesterol** (LDL <100 mg/dL)\n9. **Treat atrial fibrillation**\n10. **Regular check-ups**",
            "related": ["diet", "exercise", "blood pressure"]
        },
        
        # Risk Factors
        "risk factors": {
            "response": "**Controllable risk factors:**\n- High blood pressure (biggest risk)\n- Smoking (doubles risk)\n- Diabetes\n- High cholesterol\n- Obesity\n- Physical inactivity\n- Poor diet\n- Excessive alcohol\n- Drug abuse\n\n**Uncontrollable risk factors:**\n- Age (55+)\n- Gender (men higher risk)\n- Race (African Americans higher risk)\n- Family history\n- Previous stroke or TIA",
            "related": ["prevention", "age"]
        },
        
        "age": {
            "response": "Stroke risk doubles every decade after age 55. However, strokes can occur at any age - 15% happen to people under 45. While you can't control aging, you CAN control other risk factors. The key is early prevention: start healthy habits in your 20s-30s, get regular screenings after 40, and be extra vigilant after 55.",
            "related": ["risk factors", "prevention"]
        },
        
        # Lifestyle Factors
        "diet": {
            "response": "**Stroke-prevention diet (Mediterranean/DASH):**\n\n**EAT MORE:**\n- Fruits & vegetables (5+ servings daily)\n- Whole grains (brown rice, oats, quinoa)\n- Fish (especially fatty fish 2x/week)\n- Nuts & seeds\n- Olive oil\n- Legumes\n- Low-fat dairy\n\n**EAT LESS:**\n- Sodium (<1,500 mg/day)\n- Saturated fats\n- Trans fats\n- Red meat\n- Processed foods\n- Added sugars\n- Fried foods",
            "related": ["prevention", "blood pressure"]
        },
        
        "exercise": {
            "response": "**Exercise recommendations:**\n\n**Aerobic exercise:** 150 minutes/week of moderate activity (brisk walking, swimming, cycling) OR 75 minutes/week of vigorous activity (running, aerobics)\n\n**Strength training:** 2 days/week\n\n**Benefits:**\n- Lowers blood pressure\n- Reduces cholesterol\n- Controls weight\n- Improves circulation\n- Reduces stress\n\n**Getting started:** Start with 10-minute walks, gradually increase. Consult your doctor before starting intense exercise, especially if you have heart conditions.",
            "related": ["prevention", "weight"]
        },
        
        "weight": {
            "response": "**Healthy weight management:**\n\n**BMI ranges:**\n- Underweight: <18.5\n- Normal: 18.5-24.9\n- Overweight: 25-29.9\n- Obese: 30+\n\nExcess weight increases stroke risk by contributing to high blood pressure, diabetes, and high cholesterol. Even losing 5-10% of body weight can significantly reduce risk.\n\n**Tips:** Eat smaller portions, choose nutrient-dense foods, exercise regularly, get adequate sleep (7-9 hours), manage stress.",
            "related": ["diet", "exercise", "bmi"]
        },
        
        "bmi": {
            "response": "**BMI (Body Mass Index) = weight(kg) / height(m)²**\n\nBMI is a screening tool but has limitations (doesn't measure body fat directly). Waist circumference is also important:\n- Men: >40 inches (102 cm) = higher risk\n- Women: >35 inches (88 cm) = higher risk\n\nCombine BMI with waist measurement, body composition, and overall health for best assessment.",
            "related": ["weight", "exercise"]
        },
        
        # Medical Conditions
        "blood pressure": {
            "response": "**Blood pressure categories:**\n- Normal: <120/80 mmHg\n- Elevated: 120-129/<80\n- Stage 1 hypertension: 130-139/80-89\n- Stage 2 hypertension: ≥140/90\n- Hypertensive crisis: >180/120 (emergency!)\n\n**Management:**\n- Reduce sodium (<1,500 mg/day)\n- DASH diet\n- Regular exercise\n- Maintain healthy weight\n- Limit alcohol\n- Manage stress\n- Take medications as prescribed\n- Monitor at home\n\nHigh blood pressure is the #1 controllable risk factor for stroke!",
            "related": ["diet", "medication", "prevention"]
        },
        
        "diabetes": {
            "response": "Diabetes damages blood vessels and increases stroke risk 1.5-4 times. High blood sugar levels can:\n- Damage arteries (atherosclerosis)\n- Increase blood clots\n- Raise blood pressure\n- Increase cholesterol\n\n**Management:**\n- Keep HbA1c <7%\n- Monitor blood sugar regularly\n- Take medications as prescribed\n- Follow diabetic diet\n- Exercise regularly\n- Maintain healthy weight\n- Control blood pressure & cholesterol\n- Get regular eye and foot exams",
            "related": ["diet", "exercise", "prevention"]
        },
        
        "cholesterol": {
            "response": "**Cholesterol targets:**\n- Total cholesterol: <200 mg/dL\n- LDL (bad): <100 mg/dL (<70 if high risk)\n- HDL (good): >40 mg/dL (men), >50 (women)\n- Triglycerides: <150 mg/dL\n\n**Management:**\n- Reduce saturated fats\n- Eliminate trans fats\n- Eat more fiber (oats, beans, fruits)\n- Add omega-3 fatty acids (fish)\n- Exercise regularly\n- Maintain healthy weight\n- Take statins if prescribed\n- Get tested every 4-6 years (more often if high risk)",
            "related": ["diet", "medication", "prevention"]
        },
        
        "heart disease": {
            "response": "Heart disease and stroke share many risk factors. Conditions that increase stroke risk:\n\n**Atrial fibrillation (AFib):** Irregular heartbeat increases clot risk 5x - may need blood thinners\n\n**Coronary artery disease:** Plaque buildup narrows arteries\n\n**Heart failure:** Reduced blood flow increases clot risk\n\n**Heart valve disease:** Can cause blood clots\n\n**Previous heart attack:** Increases overall cardiovascular risk\n\nManage heart conditions with medications, lifestyle changes, and regular cardiology follow-ups.",
            "related": ["risk factors", "medication"]
        },
        
        # Habits
        "smoking": {
            "response": "Smoking **DOUBLES** your stroke risk by:\n- Thickening blood and increasing clots\n- Damaging blood vessel walls\n- Raising blood pressure\n- Reducing oxygen in blood\n- Increasing atherosclerosis\n\n**Quitting benefits:**\n- Risk drops 50% within 1 year\n- Returns to normal within 5-15 years\n- Immediate: blood pressure & heart rate drop\n\n**Quit strategies:**\n- Nicotine replacement therapy\n- Prescription medications (varenicline, bupropion)\n- Counseling\n- Support groups\n- Quitline: 1-800-QUIT-NOW\n- Mobile apps",
            "related": ["prevention", "risk factors"]
        },
        
        "alcohol": {
            "response": "**Alcohol and stroke - complex relationship:**\n\n**Moderate drinking** (may reduce ischemic stroke risk):\n- Women: 1 drink/day\n- Men: 2 drinks/day\n\n**Heavy drinking** increases risk:\n- Raises blood pressure\n- Increases triglycerides\n- Can cause atrial fibrillation\n- Increases hemorrhagic stroke risk\n- Weakens heart muscle\n\n**1 drink =**\n- 12 oz beer (5% alcohol)\n- 5 oz wine\n- 1.5 oz liquor\n\nIf you don't drink, don't start. If you drink, stay within limits.",
            "related": ["blood pressure", "prevention"]
        },
        
        "stress": {
            "response": "Chronic stress increases stroke risk through:\n- Elevated blood pressure\n- Increased inflammation\n- Unhealthy coping behaviors (smoking, overeating)\n- Sleep problems\n- Weakened immune system\n\n**Stress management techniques:**\n- Meditation & mindfulness\n- Deep breathing exercises\n- Yoga or tai chi\n- Regular exercise\n- Adequate sleep (7-9 hours)\n- Social connections\n- Hobbies & leisure activities\n- Professional counseling\n- Time management\n- Setting boundaries",
            "related": ["exercise", "sleep"]
        },
        
        "sleep": {
            "response": "Poor sleep increases stroke risk. Sleep problems linked to stroke:\n\n**Sleep apnea:** Breathing interruptions during sleep increase risk 2-3x. Symptoms: loud snoring, gasping, daytime fatigue. Treatment: CPAP machine, weight loss, positional therapy.\n\n**Insomnia:** Chronic poor sleep raises blood pressure and inflammation.\n\n**Too little/too much:** Both <6 hours and >9 hours associated with higher risk.\n\n**Tips for better sleep:**\n- Consistent sleep schedule\n- Cool, dark, quiet bedroom\n- Avoid screens before bed\n- Limit caffeine after 2pm\n- Regular exercise (not close to bedtime)\n- Relaxation techniques",
            "related": ["stress", "prevention"]
        },
        
        # Medication
        "medication": {
            "response": "**Common stroke prevention medications:**\n\n**Blood thinners:**\n- Antiplatelet: Aspirin, clopidogrel (Plavix)\n- Anticoagulants: Warfarin, apixaban (Eliquis), rivaroxaban (Xarelto)\n\n**Blood pressure:**\n- ACE inhibitors, ARBs, beta-blockers, diuretics\n\n**Cholesterol:**\n- Statins (atorvastatin, simvastatin)\n\n**Diabetes:**\n- Metformin, insulin, others\n\n**⚠️ CRITICAL:** Never stop or change medications without consulting your doctor! Even if you feel fine, medications prevent future strokes.",
            "related": ["blood pressure", "cholesterol", "diabetes"]
        },
        
        # Recovery
        "recovery": {
            "response": "**Stroke recovery timeline:**\n\n**First 3 months:** Most rapid recovery (neuroplasticity)\n**3-6 months:** Continued significant improvement\n**6-12 months:** Slower but ongoing progress\n**Beyond 1 year:** Improvement can continue for years\n\n**Rehabilitation includes:**\n- Physical therapy (mobility, strength)\n- Occupational therapy (daily activities)\n- Speech therapy (communication, swallowing)\n- Cognitive therapy (memory, problem-solving)\n- Emotional support (depression is common)\n\n**Success factors:**\n- Early intensive therapy\n- Family support\n- Patient motivation\n- Preventing another stroke",
            "related": ["rehabilitation", "prevention"]
        },
        
        "rehabilitation": {
            "response": "**Comprehensive stroke rehabilitation:**\n\n**Physical therapy:** Improves movement, balance, coordination, walking. May use assistive devices.\n\n**Occupational therapy:** Relearns daily activities (eating, dressing, bathing). Adapts home environment.\n\n**Speech-language therapy:** Addresses aphasia (language problems), dysarthria (speech problems), dysphagia (swallowing).\n\n**Cognitive therapy:** Improves memory, attention, problem-solving.\n\n**Psychological support:** Addresses depression (affects 30-50% of survivors), anxiety, emotional changes.\n\n**Duration:** Varies widely - weeks to years depending on severity. Intensity matters: more therapy = better outcomes.",
            "related": ["recovery", "support"]
        },
        
        "support": {
            "response": "**Resources for stroke survivors & caregivers:**\n\n**Organizations:**\n- American Stroke Association\n- National Stroke Association\n- Stroke Recovery Foundation\n\n**Support:**\n- Local support groups\n- Online communities\n- Counseling services\n- Caregiver support programs\n\n**Helplines:**\n- Stroke Helpline: 1-888-4-STROKE\n- Caregiver Helpline\n\n**Remember:** Depression is common after stroke - seek help. Recovery is possible with proper support and rehabilitation!",
            "related": ["recovery", "rehabilitation"]
        }
    }
    
    # Enhanced matching algorithm
    best_match = None
    best_score = 0
    
    for key, value in knowledge_base.items():
        # Calculate relevance score
        words_in_key = key.split()
        words_in_question = question_lower.split()
        
        matches = sum(1 for word in words_in_key if word in question_lower)
        score = matches / len(words_in_key) if words_in_key else 0
        
        if score > best_score:
            best_score = score
            best_match = value
    
    # Return best match if confident enough
    if best_score > 0.5 and best_match:
        response = best_match["response"]
        related = best_match.get("related", [])
        
        if related:
            response += f"\n\n**💡 Related topics:** {', '.join(related)}"
        
        return response
    
    # Default response with suggestions
    return """I'm here to help with stroke-related questions! You can ask about:

📌 **Stroke basics:** types, symptoms, causes
🚨 **Emergency:** warning signs, when to call 911
🛡️ **Prevention:** diet, exercise, lifestyle changes
🏥 **Medical:** blood pressure, diabetes, medications
🔄 **Recovery:** rehabilitation, support resources

**Try asking:** "What are stroke symptoms?" or "How can I prevent stroke?" or click a quick question button above."""


# Example integration in 6_Chatbot.py:
"""
# Replace the simple get_response() function with:

from chatbot_knowledge_base import get_enhanced_response

def get_response(question):
    return get_enhanced_response(question)
"""