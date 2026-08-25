# Golden Repository Source Excerpts

These excerpts were copied from the vectorized Golden Repository cache during specs generation.

Repository: DEVXADO,Retail Standard-365Retail
Selection mode: all vectorized files
Source excerpts: 83

## 1. Retail Standard-365Retail/business-requirements.md #0

Score: 1.000

````text
> Source: [https://nousinfoteam.atlassian.net/wiki/spaces/SCRUM/pages/2719761](https://nousinfoteam.atlassian.net/wiki/spaces/SCRUM/pages/2719761)
````

## 2. Retail Standard-365Retail/business-requirements.md #1

Score: 1.000

````text
| Field | Value |
| --- | --- |
| Document Title | Business Requirements – Project Management Capability |
| Epic | Project Management Solution for My Team |
| Version | 1.0 |
| Status | Approved |
| Organization | My Team |
| Last Updated | 2025 |
| Author | Business Analysis Team |
| Audience | Project Stakeholders, Development Team, QA, Architecture |
````

## 3. Retail Standard-365Retail/business-requirements.md #2

Score: 1.000

````text
This Business Requirements Document establishes the comprehensive requirements for a unified project management capability within the My Team organization. The solution addresses the critical business need for structured project delivery through standardized documentation, lifecycle management, task tracking, and team collaboration. This document serves as the authoritative source of truth for all functional and non-functional requirements governing the implementation of this capability within Azure DevOps.
````

## 4. Retail Standard-365Retail/business-requirements.md #3

Score: 1.000

````text
The My Team organization requires a centralized platform that enables team members to effectively plan, track, and manage project activities from initiation through completion. Currently, the absence of a unified project management system results in inconsistent documentation practices, unclear accountability, limited traceability of project decisions, and fragmented workflow processes. This solution directly addresses these deficiencies by establishing enforceable business rules, standardized documentation templates, and structured lifecycle management.
````

## 5. Retail Standard-365Retail/business-requirements.md #4

Score: 1.000

````text
The solution encompasses three primary capability areas, organized as features within a single epic:
````

## 6. Retail Standard-365Retail/business-requirements.md #5

Score: 1.000

````text
| Epic | Feature | Capability Area |
| --- | --- | --- |
| Project Management Solution for My Team | Project Lifecycle Management | Project creation, status transitions, team member association, and ownership enforcement |
| Project Management Solution for My Team | BRD Creation and Document Management | Business Requirements Document creation, editing, version management, and search/retrieval |
| Project Management Solution for My Team | Task Management and Team Collaboration | Task creation, assignment, status tracking, and personal dashboard visibility |
````

## 7. Retail Standard-365Retail/business-requirements.md #6

Score: 1.000

````text
- **Accountability**: Every project must have a designated owner, and all activities must be traceable to responsible individuals
- **Traceability**: The system must maintain auditable history of project decisions, changes, and actions
- **Workflow Integrity**: Business rules governing status transitions, data completeness, and process sequencing must be consistently enforced
- **Standardization**: Documentation processes must follow organizational standards to ensure consistency across all projects
- **Collaboration**: Team members must be able to work together effectively on shared project activities and documentation
````

## 8. Retail Standard-365Retail/business-requirements.md #7

Score: 1.000

````text
This document addresses nine (9) user stories that collectively define the functional scope of the solution. Each user story has been decomposed into detailed functional requirements with explicit traceability to BRD requirements, epics, and features. The complete mapping is maintained in Section 6 (Comprehensive Traceability Matrix).
````

## 9. Retail Standard-365Retail/business-requirements.md #8

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-1 |
| Feature | Project Lifecycle Management |
| Epic | Project Management Solution for My Team |
````

## 10. Retail Standard-365Retail/business-requirements.md #9

Score: 1.000

````text
**Description:** The system must allow team members to create new projects within the My Team organization, capturing essential project information at the time of creation. The project creation process enforces mandatory data completeness requirements, including the assignment of a project owner, before a project record can be persisted.
**Business Rules:**
- Each project must have a designated project owner assigned at the time of creation (mandatory project ownership)
- The system must display a project creation form with clearly marked mandatory fields including Project Name, Status, and Owner
- The system must prevent submission when any mandatory field is empty
- The system must set a default project status of "Not Started" upon creation
- The system must generate a unique project identifier upon successful creation
**Acceptance Criteria:**
- The system displays a project creation form with clearly marked mandatory fields (Project Name, Status, Owner) and prevents submission when any mandatory field is empty
- The system provides a dropdown of registered team members for owner selection and requires one to be selected before saving
- The system sets default project status to "Not Started" upon creation
- The system generates a unique project identifier upon successful creation
- The project is successfully created and visible within the My Team organization
- A validation error is displayed if a user attempts to save a project without completing all mandatory fields
**Traceability:**
````

## 11. Retail Standard-365Retail/business-requirements.md #10

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-1: "As Project Team Member, I want to perform project creation to achieve structured project initialization with mandatory ownership" |
| BRD Requirements | FR-001 (Project Creation), FR-002 (Mandatory Project Ownership Assignment), FR-011 (Minimum Data Completeness Enforcement) |
| Epic | Project Management Solution for My Team |
| Feature | Project Lifecycle Management |
````

## 12. Retail Standard-365Retail/business-requirements.md #11

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-2 |
| Feature | Project Lifecycle Management |
| Epic | Project Management Solution for My Team |
````

## 13. Retail Standard-365Retail/business-requirements.md #12

Score: 1.000

````text
**Description:** The system must support project lifecycle management through defined project statuses and enforce logical status transitions. Projects must progress through valid stages from initiation to completion, and the system must prevent invalid or illogical status changes.
**Business Rules:**
- Projects must follow logical status transitions; not all status changes are permitted from every state
- Valid transitions are defined as: Not Started → In Progress; In Progress → Completed
- The system must block invalid transitions (e.g., Not Started directly to Completed)
- Only valid next-status options shall be presented to the user based on the current project state
- The system must record the timestamp and user identity for each status transition
**Acceptance Criteria:**
- The system only presents valid next status options based on current project state (Not Started can only transition to In Progress; In Progress can only transition to Completed)
- The system blocks and displays an error message when an invalid status transition is attempted (e.g., Not Started directly to Completed)
- The system records the timestamp and user identity for each status transition for audit purposes
- The system reflects the current lifecycle stage of each project accurately
- An appropriate error or notification is displayed when an invalid transition is attempted
**Status Transition Model:**
````

## 14. Retail Standard-365Retail/business-requirements.md #13

Score: 1.000

````text
![Diagram
````

## 15. Retail Standard-365Retail/business-requirements.md #14

Score: 1.000

````text
1](data:image/svg+xml;charset=utf-8;base64,PHN2ZyBpZD0ibWVybWFpZERpYWdyYW0iIHdpZHRoPSI2MjguOTA2MjUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgY2xhc3M9ImZsb3djaGFydCIgaGVpZ2h0PSIxNTMiIHZpZXdCb3g9Ii0xMiAtMTIgNjI4LjkwNjI1IDE1MyIgcm9sZT0iZ3JhcGhpY3MtZG9jdW1lbnQgZG9jdW1lbnQiIGFyaWEtcm9sZWRlc2NyaXB0aW9uPSJmbG93Y2hhcnQtdjIiPjxzdHlsZT4jbWVybWFpZERpYWdyYW17Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O2ZpbGw6IzMzMzt9QGtleWZyYW1lcyBlZGdlLWFuaW1hdGlvbi1mcmFtZXtmcm9te3N0cm9rZS1kYXNob2Zmc2V0OjA7fX1Aa2V5ZnJhbWVzIGRhc2h7dG97c3Ryb2tlLWRhc2hvZmZzZXQ6MDt9fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS1hbmltYXRpb24tc2xvd3tzdHJva2UtZGFzaGFycmF5OjksNSFpbXBvcnRhbnQ7c3Ryb2tlLWRhc2hvZmZzZXQ6OTAwO2FuaW1hdGlvbjpkYXNoIDUwcyBsaW5lYXIgaW5maW5pdGU7c3Ryb2tlLWxpbmVjYXA6cm91bmQ7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS1hbmltYXRpb24tZmFzdHtzdHJva2UtZGFzaGFycmF5OjksNSFpbXBvcnRhbnQ7c3Ryb2tlLWRhc2hvZmZzZXQ6OTAwO2FuaW1hdGlvbjpkYXNoIDIwcyBsaW5lYXIgaW5maW5pdGU7c3Ryb2tlLWxpbmVjYXA6cm91bmQ7fSNtZXJtYWlkRGlhZ3JhbSAuZXJyb3ItaWNvbntmaWxsOiM1NTIyMjI7fSNtZXJtYWlkRGlhZ3JhbSAuZXJyb3ItdGV4dHtmaWxsOiM1NTIyMjI7c3Ryb2tlOiM1NTIyMjI7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS10aGlja25lc3Mtbm9ybWFse3N0cm9rZS13aWR0aDoxcHg7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS10aGlja25lc3MtdGhpY2t7c3Ryb2tlLXdpZHRoOjMuNXB4O30jbWVybWFpZERpYWdyYW0gLmVkZ2UtcGF0dGVybi1zb2xpZHtzdHJva2UtZGFzaGFycmF5OjA7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS10aGlja25lc3MtaW52aXNpYmxle3N0cm9rZS13aWR0aDowO2ZpbGw6bm9uZTt9I21lcm1haWREaWFncmFtIC5lZGdlLXBhdHRlcm4tZGFzaGVke3N0cm9rZS1kYXNoYXJyYXk6Mzt9I21lcm1haWREaWFncmFtIC5lZGdlLXBhdHRlcm4tZG90dGVke3N0cm9rZS1kYXNoYXJyYXk6Mjt9I21lcm1haWREaWFncmFtIC5tYXJrZXJ7ZmlsbDojMzMzMzMzO3N0cm9rZTojMzMzMzMzO30jbWVybWFpZERpYWdyYW0gLm1hcmtlci5jcm9zc3tzdHJva2U6IzMzMzMzMzt9I21lcm1haWREaWFncmFtIHN2Z3tmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjE2cHg7fSNtZXJtYWlkRGlhZ3JhbSBwe21hcmdpbjowO30jbWVybWFpZERpYWdyYW0gLmxhYmVse2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtjb2xvcjojMzMzO30jbWVybWFpZERpYWdyYW0gLmNsdXN0ZXItbGFiZWwgdGV4dHtmaWxsOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAuY2x1c3Rlci1sYWJlbCBzcGFue2NvbG9yOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAuY2x1c3Rlci1sYWJlbCBzcGFuIHB7YmFja2dyb3VuZC1jb2xvcjp0cmFuc3BhcmVudDt9I21lcm1haWREaWFncmFtIC5sYWJlbCB0ZXh0LCNtZXJtYWlkRGlhZ3JhbSBzcGFue2ZpbGw6IzMzMztjb2xvcjojMzMzO30jbWVybWFpZERpYWdyYW0gLm5vZGUgcmVjdCwjbWVybWFpZERpYWdyYW0gLm5vZGUgY2lyY2xlLCNtZXJtYWlkRGlhZ3JhbSAubm9kZSBlbGxpcHNlLCNtZXJtYWlkRGlhZ3JhbSAubm9kZSBwb2x5Z29uLCNtZXJtYWlkRGlhZ3JhbSAubm9kZSBwYXRoe2ZpbGw6I0VDRUNGRjtzdHJva2U6IzkzNzBEQjtzdHJva2Utd2lkdGg6MXB4O30jbWVybWFpZERpYWdyYW0gLnJvdWdoLW5vZGUgLmxhYmVsIHRleHQsI21lcm1haWREaWFncmFtIC5ub2RlIC5sYWJlbCB0ZXh0LCNtZXJtYWlkRGlhZ3JhbSAuaW1hZ2Utc2hhcGUgLmxhYmVsLCNtZXJtYWlkRGlhZ3JhbSAuaWNvbi1zaGFwZSAubGFiZWx7dGV4dC1hbmNob3I6bWlkZGxlO30jbWVybWFpZERpYWdyYW0gLm5vZGUgLmthdGV4IHBhdGh7ZmlsbDojMDAwO3N0cm9rZTojMDAwO3N0cm9rZS13aWR0aDoxcHg7fSNtZXJtYWlkRGlhZ3JhbSAucm91Z2gtbm9kZSAubGFiZWwsI21lcm1haWREaWFncmFtIC5ub2RlIC5sYWJlbCwjbWVybWFpZERpYWdyYW0gLmltYWdlLXNoYXBlIC5sYWJlbCwjbWVybWFpZERpYWdyYW0gLmljb24tc2hhcGUgLmxhYmVse3RleHQtYWxpZ246Y2VudGVyO30jbWVybWFpZERpYWdyYW0gLm5vZGUuY2xpY2thYmxle2N1cnNvcjpwb2ludGVyO30jbWVybWFpZERpYWdyYW0gLnJvb3QgLmFuY2hvciBwYXRoe2ZpbGw6IzMzMzMzMyFpbXBvcnRhbnQ7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlOiMzMzMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAuYXJyb3doZWFkUGF0aHtmaWxsOiMzMzMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZVBhdGggLnBhdGh7c3Ryb2tlOiMzMzMzMzM7c3Ryb2tlLXdpZHRoOjIuMHB4O30jbWVybWFpZERpYWdyYW0gLmZsb3djaGFydC1saW5re3N0cm9rZTojMzMzMzMzO2ZpbGw6bm9uZTt9I21lcm1haWREaWFncmFtIC5lZGdlTGFiZWx7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO3RleHQtYWxpZ246Y2VudGVyO30jbWVybWFpZERpYWdyYW0gLmVkZ2VMYWJlbCBwe2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt9I21lcm1haWREaWFncmFtIC5lZGdlTGFiZWwgcmVjdHtvcGFjaXR5OjAuNTtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7ZmlsbDpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO30jbWVybWFpZERpYWdyYW0gLmxhYmVsQmtne2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsIDIzMiwgMjMyLCAwLjUpO30jbWVybWFpZERpYWdyYW0gLmNsdXN0ZXIgcmVjdHtmaWxsOiNmZmZmZGU7c3Ryb2tlOiNhYWFhMzM7c3Ryb2tlLXdpZHRoOjFweDt9I21lcm1haWREaWFncmFtIC5jbHVzdGVyIHRleHR7ZmlsbDojMzMzO30jbWVybWFpZERpYWdyYW0gLmNsdXN0ZXIgc3Bhbntjb2xvcjojMzMzO30jbWVybWFpZERpYWdyYW0gZGl2Lm1lcm1haWRUb29sdGlwe3Bvc2l0aW9uOmFic29sdXRlO3RleHQtYWxpZ246Y2VudGVyO21heC13aWR0aDoyMDBweDtwYWRkaW5nOjJweDtmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjEycHg7YmFja2dyb3VuZDpoc2woODAsIDEwMCUsIDk2LjI3NDUwOTgwMzklKTtib3JkZXI6MXB4IHNvbGlkICNhYWFhMzM7Ym9yZGVyLXJhZGl1czoycHg7cG9pbnRlci1ldmVudHM6bm9uZTt6LWluZGV4OjEwMDt9I21lcm1haWREaWFncmFtIC5mbG93Y2hhcnRUaXRsZVRleHR7dGV4dC1hbmNob3I6bWlkZGxlO2ZvbnQtc2l6ZToxOHB4O2ZpbGw6IzMzMzt9I21lcm1haWREaWFncmFtIHJlY3QudGV4dHtmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjA7fSNtZXJtYWlkRGlhZ3JhbSAuaWNvbi1zaGFwZSwjbWVybWFpZERpYWdyYW0gLmltYWdlLXNoYXBle2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt0ZXh0LWFsaWduOmNlbnRlcjt9I21lcm1haWREaWFncmFtIC5pY29uLXNoYXBlIHAsI21lcm1haWREaWFncmFtIC5pbWFnZS1zaGFwZSBwe2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtwYWRkaW5nOjJweDt9I21lcm1haWREaWFncmFtIC5pY29uLXNoYXBlIHJlY3QsI21lcm1haWREaWFncmFtIC5pbWFnZS1zaGFwZSByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtmaWxsOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNtZXJtYWlkRGlhZ3JhbSAubGFiZWwtaWNvbntkaXNwbGF5OmlubGluZS1ibG9jaztoZWlnaHQ6MWVtO292ZXJmbG93OnZpc2libGU7dmVydGljYWwtYWxpZ246LTAuMTI1ZW07fSNtZXJtYWlkRGlhZ3JhbSAubm9kZSAubGFiZWwtaWNvbiBwYXRoe2ZpbGw6Y3VycmVudENvbG9yO3N0cm9rZTpyZXZlcnQ7c3Ryb2tlLXdpZHRoOnJldmVydDt9I21lcm1haWREaWFncmFtIDpyb290ey0tbWVybWFpZC1mb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7fTwvc3R5bGU+PGc+PG1hcmtlciBpZD0ibWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSI1IiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjgiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAwIDAgTCAxMCA1IEwgMCAxMCB6IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyI+PC9wYXRoPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludFN0YXJ0IiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSI0LjUiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iOCIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDAgNSBMIDEwIDEwIEwgMTAgMCB6IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyI+PC9wYXRoPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1jaXJjbGVFbmQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjExIiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VySGVpZ2h0PSIxMSIgb3JpZW50PSJhdXRvIj48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iNSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiPjwvY2lyY2xlPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1jaXJjbGVTdGFydCIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iLTEiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxjaXJjbGUgY3g9IjUiIGN5PSI1IiByPSI1IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLWNyb3NzRW5kIiBjbGFzcz0ibWFya2VyIGNyb3NzIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDExIDExIiByZWZYPSIxMiIgcmVmWT0iNS4yIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VySGVpZ2h0PSIxMSIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDEsMSBsIDksOSBNIDEwLDEgbCAtOSw5IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAyOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyI+PC9wYXRoPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1jcm9zc1N0YXJ0IiBjbGFzcz0ibWFya2VyIGNyb3NzIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDExIDExIiByZWZYPSItMSIgcmVmWT0iNS4yIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VySGVpZ2h0PSIxMSIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDEsMSBsIDksOSBNIDEwLDEgbCAtOSw5IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAyOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyI+PC9wYXRoPjwvbWFya2VyPjxnIGNsYXNzPSJyb290Ij48ZyBjbGFzcz0iY2x1c3RlcnMiPjwvZz48ZyBjbGFzcz0iZWRnZVBhdGhzIj48cGF0aCBkPSJNMTQ4LjkzOCw0OC44NTdMMTU1Ljk3LDQ2LjU0OEMxNjMuMDAzLDQ0LjIzOCwxNzcuMDY4LDM5LjYxOSwxOTAuNDY2LDM3LjMxQzIwMy44NjUsMzUsMjE2LjU5NiwzNSwyMjIuOTYyLDM1TDIyOS4zMjgsMzUiIGlkPSJMX0FfQl8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9BX0JfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TVRRNExqa3pOelVzSW5raU9qUTRMamcxTnpNMk1EYzVNekk0TnpVM2ZTeDdJbmdpT2pFNU1TNHhNekk0TVRJMUxDSjVJam96Tlgwc2V5SjRJam95TXpNdU16STRNVEkxTENKNUlqb3pOWDFkIiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMzc1LjE0MSwzNUwzODIuMTczLDM1QzM4OS4yMDYsMzUsNDAzLjI3MSwzNSw0MTYuNzA0LDM3LjEzNkM0MzAuMTM2LDM5LjI3MSw0NDIuOTM3LDQzLjU0Myw0NDkuMzM3LDQ1LjY3OEw0NTUuNzM3LDQ3LjgxNCIgaWQ9IkxfQl9DXzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0JfQ18wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNemMxTGpFME1EWXlOU3dpZVNJNk16VjlMSHNpZUNJNk5ERTNMak16TlRrek56VXNJbmtpT2pNMWZTeDdJbmdpT2pRMU9TNDFNekV5TlN3aWVTSTZORGt1TURjNU9UWTRPVGs0T0RBeU1qTjlYUT09IiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMTQ4LjkzOCw5NS4xNDNMMTU1Ljk3LDk3LjQ1MkMxNjMuMDAzLDk5Ljc2MiwxNzcuMDY4LDEwNC4zODEsMjAyLjk1MSwxMDYuNjlDMjI4LjgzMywxMDksMjY2LjUzNCwxMDksMzA0LjIzNCwxMDlDMzQxLjkzNSwxMDksMzc5LjYzNSwxMDksNDA0Ljg4NiwxMDYuODY0QzQzMC4xMzYsMTA0LjcyOSw0NDIuOTM3LDEwMC40NTcsNDQ5LjMzNyw5OC4zMjJMNDU1LjczNyw5Ni4xODYiIGlkPSJMX0FfQ18wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tZG90dGVkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfQV9DXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UUTRMamt6TnpVc0lua2lPamsxTGpFME1qWXpPVEl3TmpjeE1qUXpmU3g3SW5naU9qRTVNUzR4TXpJNE1USTFMQ0o1SWpveE1EbDlMSHNpZUNJNk16QTBMakl6TkRNM05Td2llU0k2TVRBNWZTeDdJbmdpT2pReE55NHpNelU1TXpjMUxDSjVJam94TURsOUxIc2llQ0k2TkRVNUxqVXpNVEkxTENKNUlqbzVOQzQ1TWpBd016RXdNREV4T1RjM04zMWQiIG1hcmtlci1lbmQ9InVybCgjbWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSI+PC9wYXRoPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVscyI+PGcgY2xhc3M9ImVkZ2VMYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTkxLjEzMjgxMjUsIDM1KSI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX0FfQl8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTcuMTk1MzEyNSwgLTEyKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjM0LjM5MDYyNSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjxwPlZhbGlkPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MTcuMzM1OTM3NSwgMzUpIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfQl9DXzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xNy4xOTUzMTI1LCAtMTIpIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMzQuMzkwNjI1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PHA+VmFsaWQ8L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMwNC4yMzQzNzUsIDEwOSkiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9BX0NfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTIzLjEyNSwgLTEyKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjQ2LjI1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PHA+SW52YWxpZDwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PC9nPjxnIGNsYXNzPSJub2RlcyI+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LUEtMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzguNDY4NzUsIDcyKSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTcwLjQ2ODc1IiB5PSItMjciIHdpZHRoPSIxNDAuOTM3NSIgaGVpZ2h0PSI1NCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQwLjQ2ODc1LCAtMTIpIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjgwLjkzNzUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+Tm90IFN0YXJ0ZWQ8L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1CLTEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMwNC4yMzQzNzUsIDM1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTcwLjkwNjI1IiB5PSItMjciIHdpZHRoPSIxNDEuODEyNSIgaGVpZ2h0PSI1NCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQwLjkwNjI1LCAtMTIpIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjgxLjgxMjUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+SW4gUHJvZ3Jlc3M8L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1DLTMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDUyOC4yMTg3NSwgNzIpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItNjguNjg3NSIgeT0iLTI3IiB3aWR0aD0iMTM3LjM3NSIgaGVpZ2h0PSI1NCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTM4LjY4NzUsIC0xMikiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iNzcuMzc1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPkNvbXBsZXRlZDwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PC9nPjwvZz48L2c+PC9zdmc+)
````

## 16. Retail Standard-365Retail/business-requirements.md #15

Score: 1.000

````text
**Traceability:**
````

## 17. Retail Standard-365Retail/business-requirements.md #16

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-2: "As Project Team Member, I want to perform project status transition to achieve accurate project lifecycle tracking" |
| BRD Requirements | FR-003 (Project Lifecycle Status Management), FR-004 (Logical Status Transition Enforcement), FR-014 (Workflow Integrity Enforcement) |
| Epic | Project Management Solution for My Team |
| Feature | Project Lifecycle Management |
````

## 18. Retail Standard-365Retail/business-requirements.md #17

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-3 |
| Feature | Project Lifecycle Management |
| Epic | Project Management Solution for My Team |
````

## 19. Retail Standard-365Retail/business-requirements.md #18

Score: 1.000

````text
**Description:** The system must allow project owners to associate registered team members with a project and assign project-specific roles. This capability ensures traceable project participation and supports accountability by restricting project activities to associated members only.
**Business Rules:**
- Only the project owner may add team members to a project
- Each team member must be assigned a project-specific role upon addition
- Duplicate team member associations are not permitted
- Only team members associated with a project may perform activities within that project context
- The system must maintain a record of team member associations for traceability purposes
**Acceptance Criteria:**
- The system allows the project owner to add registered team members to a project and assigns them a project-specific role upon addition
- The system prevents duplicate team member associations and displays an error if a member already associated is selected again
- The system enforces that only team members associated with a project can perform project-specific activities (task assignment, BRD editing)
- The system maintains a visible roster of associated team members with their assigned roles
- Team member association changes are logged for audit purposes
**Traceability:**
````

## 20. Retail Standard-365Retail/business-requirements.md #19

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-3: "As Project Team Member, I want to perform team member association to achieve traceable project participation" |
| BRD Requirements | FR-010 (Team Collaboration), FR-013 (Accountability and Traceability Support) |
| Epic | Project Management Solution for My Team |
| Feature | Project Lifecycle Management |
````

## 21. Retail Standard-365Retail/business-requirements.md #20

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-4 |
| Feature | BRD Creation and Document Management |
| Epic | Project Management Solution for My Team |
````

## 22. Retail Standard-365Retail/business-requirements.md #21

Score: 1.000

````text
**Description:** The system must allow team members to create Business Requirements Documents (BRDs) associated with a project using a standardized template structure. The BRD creation process enforces organizational documentation standards and auto-populates document control information to reduce manual effort and ensure consistency.
**Business Rules:**
- BRDs must follow a standardized structure/format defined by the organization
- The standardized template must include sections for: Executive Summary, Purpose & Scope, Business Objectives, Functional Requirements, and Non-Functional Requirements
- Document control fields (project name, creation date, version number, author) must be auto-populated by the system
- A BRD must be associated with exactly one parent project
- The initial version of a BRD is set to 1.0 upon creation
- Initial BRD status is set to "Draft" upon creation
**Acceptance Criteria:**
- The system displays a BRD creation form with standardized template sections (Executive Summary, Purpose & Scope, Business Objectives, Functional Requirements, Non-Functional Requirements) when user initiates BRD creation within a project
- The system auto-populates document control fields (project name, creation date, version number, author) upon BRD creation
- The system sets initial BRD version to 1.0 and status to "Draft" upon creation
- The created BRD is saved and associated with the relevant project
- The BRD follows the structured, standardized format consistently
**Traceability:**
````

## 23. Retail Standard-365Retail/business-requirements.md #22

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-4: "As Project Team Member, I want to perform BRD creation to achieve standardized project documentation" |
| BRD Requirements | FR-005 (BRD Creation), FR-015 (Standardized Documentation Processes), FR-011 (Minimum Data Completeness Enforcement) |
| Epic | Project Management Solution for My Team |
| Feature | BRD Creation and Document Management |
````

## 24. Retail Standard-365Retail/business-requirements.md #23

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-5 |
| Feature | BRD Creation and Document Management |
| Epic | Project Management Solution for My Team |
````

## 25. Retail Standard-365Retail/business-requirements.md #24

Score: 1.000

````text
**Description:** The system must allow team members to edit existing Business Requirements Documents and manage document versions. The version management capability ensures that changes are tracked, previous versions are preserved, and a complete audit trail of document evolution is maintained.
**Business Rules:**
- Changes saved as draft do not increment the version number
- Version number is automatically incremented only when the user explicitly publishes an edited BRD
- A change summary is required before publishing a new version
- The system must maintain a complete version history showing all published versions with date, author, and change summary
- Previous versions must remain accessible in read-only format
- Only team members associated with the parent project may edit BRDs within that project
**Acceptance Criteria:**
- The system allows editing of existing BRD content and saves changes as draft without incrementing version number until explicitly published
- The system automatically increments version number when user publishes edited BRD and requires a change summary before publishing
- The system maintains a complete version history showing all published versions with date, author, and change summary
- Previous versions remain accessible in read-only format for reference and audit purposes
- Changes to a BRD are saved and persisted correctly
- Users can organize and locate BRDs within the system
**Traceability:**
````

## 26. Retail Standard-365Retail/business-requirements.md #25

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-5: "As Project Team Member, I want to perform BRD editing and version management to achieve maintained documentation accuracy" |
| BRD Requirements | FR-006 (BRD Management), FR-013 (Accountability and Traceability Support), FR-012 (Project Documentation Organization) |
| Epic | Project Management Solution for My Team |
| Feature | BRD Creation and Document Management |
````

## 27. Retail Standard-365Retail/business-requirements.md #26

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-6 |
| Feature | BRD Creation and Document Management |
| Epic | Project Management Solution for My Team |
````

## 28. Retail Standard-365Retail/business-requirements.md #27

Score: 1.000

````text
**Description:** The system must provide comprehensive search and retrieval capabilities for Business Requirements Documents, enabling team members to efficiently discover and access relevant documentation. Search results must respect project access boundaries and provide contextual information to aid document identification.
**Business Rules:**
- Full-text search must span BRD titles and content
- Search results must return within 2 seconds
- Results must include relevant context snippets to aid identification
- Filtering must be available by project, status (Draft/Published), author, and date range
- Search results must be restricted to only BRDs within projects the user is associated with
- The system must display the most recent version of each BRD in search results by default
**Acceptance Criteria:**
- The system provides full-text search across BRD titles and content, returning results with relevant context snippets within 2 seconds
- The system allows filtering search results by project, status (Draft/Published), author, and date range with dynamic result updates
- The system restricts search results to only BRDs within projects the user is associated with (access boundary enforcement)
- The system displays the most recent version of each BRD in search results by default
- Users can navigate to and locate project documents efficiently from search results
**Traceability:**
````

## 29. Retail Standard-365Retail/business-requirements.md #28

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-6: "As Project Team Member, I want to perform BRD search and retrieval to achieve efficient document discovery" |
| BRD Requirements | FR-012 (Project Documentation Organization), FR-006 (BRD Management) |
| Epic | Project Management Solution for My Team |
| Feature | BRD Creation and Document Management |
````

## 30. Retail Standard-365Retail/business-requirements.md #29

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-7 |
| Feature | Task Management and Team Collaboration |
| Epic | Project Management Solution for My Team |
````

## 31. Retail Standard-365Retail/business-requirements.md #30

Score: 1.000

````text
**Description:** The system must provide task creation and assignment capabilities, allowing team members to define granular work items within a project context. Tasks enable detailed work breakdown and assignment to specific team members for execution and tracking.
**Business Rules:**
- Task Title is a mandatory field; Description, Priority, Due Date, and Assignee are optional
- Assignee selection must be restricted to team members currently associated with the project
- The system must display an error if a non-associated member is assigned via API
- The system must set initial task status to "To Do" upon creation
- Tasks must be associated with exactly one parent project
- The system must generate a unique task identifier upon creation
**Acceptance Criteria:**
- The system displays task creation form with mandatory Title field and optional Description, Priority, Due Date, and Assignee fields within the project context
- The system restricts assignee selection to only team members currently associated with the project and displays error if non-associated member is assigned via API
- The system sets initial task status to "To Do" upon creation
- The system generates a unique task identifier upon creation
- Tasks can be assigned to team members and task progress is visible to relevant team members
- Created tasks are visible within the parent project context
**Traceability:**
````

## 32. Retail Standard-365Retail/business-requirements.md #31

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-7: "As Project Team Member, I want to perform task creation and assignment to achieve granular work tracking within projects" |
| BRD Requirements | FR-009 (Task Tracking), FR-007 (Project Activity Planning), FR-011 (Minimum Data Completeness Enforcement) |
| Epic | Project Management Solution for My Team |
| Feature | Task Management and Team Collaboration |
````

## 33. Retail Standard-365Retail/business-requirements.md #32

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-8 |
| Feature | Task Management and Team Collaboration |
| Epic | Project Management Solution for My Team |
````

## 34. Retail Standard-365Retail/business-requirements.md #33

Score: 1.000

````text
**Description:** The system must enable authorized team members to update task statuses, enforcing valid status transitions and access controls. Task status updates provide accurate progress tracking and maintain workflow integrity at the task level.
**Business Rules:**
- Only the task assignee or project owner may update task status; other team members are blocked with an appropriate error message
- Valid task status transitions are enforced: To Do → In Progress → Done
- Only valid next statuses are displayed based on the current task state
- Task status updates must be reflected immediately upon save
- The system must record the timestamp and user identity for each status change
- Completed task percentage must be automatically recalculated at the project level upon task status changes
**Acceptance Criteria:**
- The system allows task assignee or project owner to update task status and blocks status updates from other team members with appropriate error message
- The system enforces valid status transitions (To Do → In Progress → Done) and only displays valid next statuses based on current state
- The system updates task status immediately upon save and reflects the change across all relevant views
- The system records timestamp and user identity for each task status change
- Project-level completion metrics are automatically recalculated upon task status changes
**Task Status Transition Model:**
````

## 35. Retail Standard-365Retail/business-requirements.md #34

Score: 1.000

````text
![Diagram
````

## 36. Retail Standard-365Retail/business-requirements.md #35

Score: 1.000

````text
2](data:image/svg+xml;charset=utf-8;base64,PHN2ZyBpZD0ibWVybWFpZERpYWdyYW0iIHdpZHRoPSI1NTAuNjQwNjI1IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJmbG93Y2hhcnQiIGhlaWdodD0iMTUzIiB2aWV3Qm94PSItMTIgLTEyIDU1MC42NDA2MjUgMTUzIiByb2xlPSJncmFwaGljcy1kb2N1bWVudCBkb2N1bWVudCIgYXJpYS1yb2xlZGVzY3JpcHRpb249ImZsb3djaGFydC12MiI+PHN0eWxlPiNtZXJtYWlkRGlhZ3JhbXtmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjE2cHg7ZmlsbDojMzMzO31Aa2V5ZnJhbWVzIGVkZ2UtYW5pbWF0aW9uLWZyYW1le2Zyb217c3Ryb2tlLWRhc2hvZmZzZXQ6MDt9fUBrZXlmcmFtZXMgZGFzaHt0b3tzdHJva2UtZGFzaG9mZnNldDowO319I21lcm1haWREaWFncmFtIC5lZGdlLWFuaW1hdGlvbi1zbG93e3N0cm9rZS1kYXNoYXJyYXk6OSw1IWltcG9ydGFudDtzdHJva2UtZGFzaG9mZnNldDo5MDA7YW5pbWF0aW9uOmRhc2ggNTBzIGxpbmVhciBpbmZpbml0ZTtzdHJva2UtbGluZWNhcDpyb3VuZDt9I21lcm1haWREaWFncmFtIC5lZGdlLWFuaW1hdGlvbi1mYXN0e3N0cm9rZS1kYXNoYXJyYXk6OSw1IWltcG9ydGFudDtzdHJva2UtZGFzaG9mZnNldDo5MDA7YW5pbWF0aW9uOmRhc2ggMjBzIGxpbmVhciBpbmZpbml0ZTtzdHJva2UtbGluZWNhcDpyb3VuZDt9I21lcm1haWREaWFncmFtIC5lcnJvci1pY29ue2ZpbGw6IzU1MjIyMjt9I21lcm1haWREaWFncmFtIC5lcnJvci10ZXh0e2ZpbGw6IzU1MjIyMjtzdHJva2U6IzU1MjIyMjt9I21lcm1haWREaWFncmFtIC5lZGdlLXRoaWNrbmVzcy1ub3JtYWx7c3Ryb2tlLXdpZHRoOjFweDt9I21lcm1haWREaWFncmFtIC5lZGdlLXRoaWNrbmVzcy10aGlja3tzdHJva2Utd2lkdGg6My41cHg7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS1wYXR0ZXJuLXNvbGlke3N0cm9rZS1kYXNoYXJyYXk6MDt9I21lcm1haWREaWFncmFtIC5lZGdlLXRoaWNrbmVzcy1pbnZpc2libGV7c3Ryb2tlLXdpZHRoOjA7ZmlsbDpub25lO30jbWVybWFpZERpYWdyYW0gLmVkZ2UtcGF0dGVybi1kYXNoZWR7c3Ryb2tlLWRhc2hhcnJheTozO30jbWVybWFpZERpYWdyYW0gLmVkZ2UtcGF0dGVybi1kb3R0ZWR7c3Ryb2tlLWRhc2hhcnJheToyO30jbWVybWFpZERpYWdyYW0gLm1hcmtlcntmaWxsOiMzMzMzMzM7c3Ryb2tlOiMzMzMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAubWFya2VyLmNyb3Nze3N0cm9rZTojMzMzMzMzO30jbWVybWFpZERpYWdyYW0gc3Zne2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTZweDt9I21lcm1haWREaWFncmFtIHB7bWFyZ2luOjA7fSNtZXJtYWlkRGlhZ3JhbSAubGFiZWx7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2NvbG9yOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAuY2x1c3Rlci1sYWJlbCB0ZXh0e2ZpbGw6IzMzMzt9I21lcm1haWREaWFncmFtIC5jbHVzdGVyLWxhYmVsIHNwYW57Y29sb3I6IzMzMzt9I21lcm1haWREaWFncmFtIC5jbHVzdGVyLWxhYmVsIHNwYW4gcHtiYWNrZ3JvdW5kLWNvbG9yOnRyYW5zcGFyZW50O30jbWVybWFpZERpYWdyYW0gLmxhYmVsIHRleHQsI21lcm1haWREaWFncmFtIHNwYW57ZmlsbDojMzMzO2NvbG9yOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAubm9kZSByZWN0LCNtZXJtYWlkRGlhZ3JhbSAubm9kZSBjaXJjbGUsI21lcm1haWREaWFncmFtIC5ub2RlIGVsbGlwc2UsI21lcm1haWREaWFncmFtIC5ub2RlIHBvbHlnb24sI21lcm1haWREaWFncmFtIC5ub2RlIHBhdGh7ZmlsbDojRUNFQ0ZGO3N0cm9rZTojOTM3MERCO3N0cm9rZS13aWR0aDoxcHg7fSNtZXJtYWlkRGlhZ3JhbSAucm91Z2gtbm9kZSAubGFiZWwgdGV4dCwjbWVybWFpZERpYWdyYW0gLm5vZGUgLmxhYmVsIHRleHQsI21lcm1haWREaWFncmFtIC5pbWFnZS1zaGFwZSAubGFiZWwsI21lcm1haWREaWFncmFtIC5pY29uLXNoYXBlIC5sYWJlbHt0ZXh0LWFuY2hvcjptaWRkbGU7fSNtZXJtYWlkRGlhZ3JhbSAubm9kZSAua2F0ZXggcGF0aHtmaWxsOiMwMDA7c3Ryb2tlOiMwMDA7c3Ryb2tlLXdpZHRoOjFweDt9I21lcm1haWREaWFncmFtIC5yb3VnaC1ub2RlIC5sYWJlbCwjbWVybWFpZERpYWdyYW0gLm5vZGUgLmxhYmVsLCNtZXJtYWlkRGlhZ3JhbSAuaW1hZ2Utc2hhcGUgLmxhYmVsLCNtZXJtYWlkRGlhZ3JhbSAuaWNvbi1zaGFwZSAubGFiZWx7dGV4dC1hbGlnbjpjZW50ZXI7fSNtZXJtYWlkRGlhZ3JhbSAubm9kZS5jbGlja2FibGV7Y3Vyc29yOnBvaW50ZXI7fSNtZXJtYWlkRGlhZ3JhbSAucm9vdCAuYW5jaG9yIHBhdGh7ZmlsbDojMzMzMzMzIWltcG9ydGFudDtzdHJva2Utd2lkdGg6MDtzdHJva2U6IzMzMzMzMzt9I21lcm1haWREaWFncmFtIC5hcnJvd2hlYWRQYXRoe2ZpbGw6IzMzMzMzMzt9I21lcm1haWREaWFncmFtIC5lZGdlUGF0aCAucGF0aHtzdHJva2U6IzMzMzMzMztzdHJva2Utd2lkdGg6Mi4wcHg7fSNtZXJtYWlkRGlhZ3JhbSAuZmxvd2NoYXJ0LWxpbmt7c3Ryb2tlOiMzMzMzMzM7ZmlsbDpub25lO30jbWVybWFpZERpYWdyYW0gLmVkZ2VMYWJlbHtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7dGV4dC1hbGlnbjpjZW50ZXI7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZUxhYmVsIHB7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO30jbWVybWFpZERpYWdyYW0gLmVkZ2VMYWJlbCByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtmaWxsOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNtZXJtYWlkRGlhZ3JhbSAubGFiZWxCa2d7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwgMjMyLCAyMzIsIDAuNSk7fSNtZXJtYWlkRGlhZ3JhbSAuY2x1c3RlciByZWN0e2ZpbGw6I2ZmZmZkZTtzdHJva2U6I2FhYWEzMztzdHJva2Utd2lkdGg6MXB4O30jbWVybWFpZERpYWdyYW0gLmNsdXN0ZXIgdGV4dHtmaWxsOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSAuY2x1c3RlciBzcGFue2NvbG9yOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSBkaXYubWVybWFpZFRvb2x0aXB7cG9zaXRpb246YWJzb2x1dGU7dGV4dC1hbGlnbjpjZW50ZXI7bWF4LXdpZHRoOjIwMHB4O3BhZGRpbmc6MnB4O2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTJweDtiYWNrZ3JvdW5kOmhzbCg4MCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpO2JvcmRlcjoxcHggc29saWQgI2FhYWEzMztib3JkZXItcmFkaXVzOjJweDtwb2ludGVyLWV2ZW50czpub25lO3otaW5kZXg6MTAwO30jbWVybWFpZERpYWdyYW0gLmZsb3djaGFydFRpdGxlVGV4dHt0ZXh0LWFuY2hvcjptaWRkbGU7Zm9udC1zaXplOjE4cHg7ZmlsbDojMzMzO30jbWVybWFpZERpYWdyYW0gcmVjdC50ZXh0e2ZpbGw6bm9uZTtzdHJva2Utd2lkdGg6MDt9I21lcm1haWREaWFncmFtIC5pY29uLXNoYXBlLCNtZXJtYWlkRGlhZ3JhbSAuaW1hZ2Utc2hhcGV7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO3RleHQtYWxpZ246Y2VudGVyO30jbWVybWFpZERpYWdyYW0gLmljb24tc2hhcGUgcCwjbWVybWFpZERpYWdyYW0gLmltYWdlLXNoYXBlIHB7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO3BhZGRpbmc6MnB4O30jbWVybWFpZERpYWdyYW0gLmljb24tc2hhcGUgcmVjdCwjbWVybWFpZERpYWdyYW0gLmltYWdlLXNoYXBlIHJlY3R7b3BhY2l0eTowLjU7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO2ZpbGw6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt9I21lcm1haWREaWFncmFtIC5sYWJlbC1pY29ue2Rpc3BsYXk6aW5saW5lLWJsb2NrO2hlaWdodDoxZW07b3ZlcmZsb3c6dmlzaWJsZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTt9I21lcm1haWREaWFncmFtIC5ub2RlIC5sYWJlbC1pY29uIHBhdGh7ZmlsbDpjdXJyZW50Q29sb3I7c3Ryb2tlOnJldmVydDtzdHJva2Utd2lkdGg6cmV2ZXJ0O30jbWVybWFpZERpYWdyYW0gOnJvb3R7LS1tZXJtYWlkLWZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjt9PC9zdHlsZT48Zz48bWFya2VyIGlkPSJtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRFbmQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjUiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iOCIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDAgMCBMIDEwIDUgTCAwIDEwIHoiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ij48L3BhdGg+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50U3RhcnQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjQuNSIgcmVmWT0iNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI4IiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMCA1IEwgMTAgMTAgTCAxMCAwIHoiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ij48L3BhdGg+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLWNpcmNsZUVuZCIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iMTEiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxjaXJjbGUgY3g9IjUiIGN5PSI1IiByPSI1IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLWNpcmNsZVN0YXJ0IiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSItMSIgcmVmWT0iNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTEiIG1hcmtlckhlaWdodD0iMTEiIG9yaWVudD0iYXV0byI+PGNpcmNsZSBjeD0iNSIgY3k9IjUiIHI9IjUiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ij48L2NpcmNsZT48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItY3Jvc3NFbmQiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIHJlZlg9IjEyIiByZWZZPSI1LjIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ij48L3BhdGg+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLWNyb3NzU3RhcnQiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIHJlZlg9Ii0xIiByZWZZPSI1LjIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ij48L3BhdGg+PC9tYXJrZXI+PGcgY2xhc3M9InJvb3QiPjxnIGNsYXNzPSJjbHVzdGVycyI+PC9nPjxnIGNsYXNzPSJlZGdlUGF0aHMiPjxwYXRoIGQ9Ik0xMDkuNzk3LDUxLjc3TDExNi44MjksNDguOTc1QzEyMy44NjIsNDYuMTgsMTM3LjkyNyw0MC41OSwxNTEuMzI2LDM3Ljc5NUMxNjQuNzI0LDM1LDE3Ny40NTYsMzUsMTgzLjgyMiwzNUwxOTAuMTg4LDM1IiBpZD0iTF9BX0JfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfQV9CXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UQTVMamM1TmpnM05Td2llU0k2TlRFdU56Y3dORGMyTmpjd01ESXpOWDBzZXlKNElqb3hOVEV1T1RreU1UZzNOU3dpZVNJNk16VjlMSHNpZUNJNk1UazBMakU0TnpVc0lua2lPak0xZlYwPSIgbWFya2VyLWVuZD0idXJsKCNtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIj48L3BhdGg+PHBhdGggZD0iTTMzNiwzNUwzNDMuMDMzLDM1QzM1MC4wNjUsMzUsMzY0LjEzLDM1LDM3Ny41NzcsMzcuNTk5QzM5MS4wMjUsNDAuMTk4LDQwMy44NTQsNDUuMzk2LDQxMC4yNjksNDcuOTk1TDQxNi42ODMsNTAuNTk0IiBpZD0iTF9CX0NfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfQl9DXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk16TTJMQ0o1SWpvek5YMHNleUo0SWpvek56Z3VNVGsxTXpFeU5Td2llU0k2TXpWOUxIc2llQ0k2TkRJd0xqTTVNRFl5TlN3aWVTSTZOVEl1TURrMk1UVTROemd4TnpZd05qTjlYUT09IiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMTA5Ljc5Nyw5Mi4yM0wxMTYuODI5LDk1LjAyNUMxMjMuODYyLDk3LjgyLDEzNy45MjcsMTAzLjQxLDE2My44MSwxMDYuMjA1QzE4OS42OTMsMTA5LDIyNy4zOTMsMTA5LDI2NS4wOTQsMTA5QzMwMi43OTQsMTA5LDM0MC40OTUsMTA5LDM2NS43NiwxMDYuNDAxQzM5MS4wMjUsMTAzLjgwMiw0MDMuODU0LDk4LjYwNCw0MTAuMjY5LDk2LjAwNUw0MTYuNjgzLDkzLjQwNiIgaWQ9IkxfQV9DXzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1kb3R0ZWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9BX0NfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TVRBNUxqYzVOamczTlN3aWVTSTZPVEl1TWpJNU5USXpNekk1T1RjMk5YMHNleUo0SWpveE5URXVPVGt5TVRnM05Td2llU0k2TVRBNWZTeDdJbmdpT2pJMk5TNHdPVE0zTlN3aWVTSTZNVEE1ZlN4N0luZ2lPak0zT0M0eE9UVXpNVEkxTENKNUlqb3hNRGw5TEhzaWVDSTZOREl3TGpNNU1EWXlOU3dpZVNJNk9URXVPVEF6T0RReE1qRTRNak01TXpaOVhRPT0iIG1hcmtlci1lbmQ9InVybCgjbWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSI+PC9wYXRoPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVscyI+PGcgY2xhc3M9ImVkZ2VMYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTUxLjk5MjE4NzUsIDM1KSI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX0FfQl8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTcuMTk1MzEyNSwgLTEyKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjM0LjM5MDYyNSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjxwPlZhbGlkPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzNzguMTk1MzEyNSwgMzUpIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfQl9DXzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xNy4xOTUzMTI1LCAtMTIpIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMzQuMzkwNjI1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PHA+VmFsaWQ8L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2NS4wOTM3NSwgMTA5KSI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX0FfQ18wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjMuMTI1LCAtMTIpIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iNDYuMjUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwgIj48cD5JbnZhbGlkPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PGcgY2xhc3M9Im5vZGVzIj48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtQS0wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg1OC44OTg0Mzc1LCA3MikiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii01MC44OTg0Mzc1IiB5PSItMjciIHdpZHRoPSIxMDEuNzk2ODc1IiBoZWlnaHQ9IjU0Ij48L3JlY3Q+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjAuODk4NDM3NSwgLTEyKSI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IHdpZHRoPSI0MS43OTY4NzUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+VG8gRG88L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1CLTEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2NS4wOTM3NSwgMzUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItNzAuOTA2MjUiIHk9Ii0yNyIgd2lkdGg9IjE0MS44MTI1IiBoZWlnaHQ9IjU0Ij48L3JlY3Q+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDAuOTA2MjUsIC0xMikiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iODEuODEyNSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD5JbiBQcm9ncmVzczwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LUMtMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNDY5LjUxNTYyNSwgNzIpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItNDkuMTI1IiB5PSItMjciIHdpZHRoPSI5OC4yNSIgaGVpZ2h0PSI1NCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTE5LjEyNSwgLTEyKSI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IHdpZHRoPSIzOC4yNSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD5Eb25lPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PC9nPjwvZz48L3N2Zz4=)
````

## 37. Retail Standard-365Retail/business-requirements.md #36

Score: 1.000

````text
**Traceability:**
````

## 38. Retail Standard-365Retail/business-requirements.md #37

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-8: "As Project Team Member, I want to perform task status updates to achieve accurate progress tracking" |
| BRD Requirements | FR-008 (Project Activity Tracking), FR-009 (Task Tracking), FR-004 (Logical Status Transition Enforcement), FR-014 (Workflow Integrity Enforcement) |
| Epic | Project Management Solution for My Team |
| Feature | Task Management and Team Collaboration |
````

## 39. Retail Standard-365Retail/business-requirements.md #38

Score: 1.000

````text
| Attribute | Detail |
| --- | --- |
| Priority | High |
| Source Story | story-9 |
| Feature | Task Management and Team Collaboration |
| Epic | Project Management Solution for My Team |
````

## 40. Retail Standard-365Retail/business-requirements.md #39

Score: 1.000

````text
**Description:** The system must provide a personal task dashboard that consolidates all tasks assigned to a team member across all projects, providing a unified view of individual workload and enabling efficient work prioritization and progress monitoring.
**Business Rules:**
- The dashboard must display all tasks assigned to the logged-in user across all projects they are associated with
- Tasks must be organized or sortable by project, status, priority, and due date
- The dashboard must reflect real-time or near-real-time task status information
- Overdue tasks (past due date with status not "Done") must be visually highlighted
- The dashboard must provide direct navigation to task details and parent project context
**Acceptance Criteria:**
- The system displays a personal dashboard showing all tasks assigned to the current user across all associated projects
- Tasks on the dashboard are organized by project and sortable by status, priority, and due date
- The dashboard reflects current task status information in real-time or near-real-time
- Overdue tasks are visually highlighted to draw attention to items requiring immediate action
- Users can navigate directly from a dashboard task to the full task detail view and parent project
- Tracking information is accessible to relevant team members from the dashboard view
**Traceability:**
````

## 41. Retail Standard-365Retail/business-requirements.md #40

Score: 1.000

````text
| Dimension | Reference |
| --- | --- |
| User Story | story-9: "As Project Team Member, I want to perform personal task dashboard viewing to achieve consolidated work visibility across projects" |
| BRD Requirements | FR-008 (Project Activity Tracking), FR-009 (Task Tracking), FR-010 (Team Collaboration) |
| Epic | Project Management Solution for My Team |
| Feature | Task Management and Team Collaboration |
````

## 42. Retail Standard-365Retail/business-requirements.md #41

Score: 1.000

````text
| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-001 | BRD search results must return within acceptable response time | ≤ 2 seconds |
| NFR-002 | Task status updates must be reflected immediately upon save | Real-time |
| NFR-003 | Project creation form must load within acceptable time | ≤ 3 seconds |
| NFR-004 | Dashboard data must refresh to reflect current state | Near-real-time (≤ 5 seconds) |
| NFR-005 | Page load times for all system views must remain responsive under normal load | ≤ 3 seconds |
````

## 43. Retail Standard-365Retail/business-requirements.md #42

Score: 1.000

````text
| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-006 | The system must support the current My Team organization membership | All registered team members |
| NFR-007 | The system must support multiple concurrent projects without degradation | Minimum 50 active projects |
| NFR-008 | BRD storage must accommodate version history growth over time | Unlimited version retention |
| NFR-009 | Task volume per project must support granular work breakdown | Minimum 200 tasks per project |
````

## 44. Retail Standard-365Retail/business-requirements.md #43

Score: 1.000

````text
| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-010 | Access to project data must be restricted to associated team members only | Role-based access control |
| NFR-011 | BRD search results must respect project access boundaries | Enforced at query level |
| NFR-012 | Task status updates must be restricted to authorized users (assignee or owner) | Permission enforcement |
| NFR-013 | All user actions must be attributable to an authenticated identity | Audit trail requirement |
````

## 45. Retail Standard-365Retail/business-requirements.md #44

Score: 1.000

````text
| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-014 | The system must persist all saved data without loss | 99.9% data integrity |
| NFR-015 | Version history must be immutable once published | No modification of published versions |
| NFR-016 | Business rule enforcement must be consistent across all access methods (UI and API) | 100% consistency |
````

## 46. Retail Standard-365Retail/business-requirements.md #45

Score: 1.000

````text
| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-017 | Mandatory fields must be clearly marked on all forms | Visual indicators on all required fields |
| NFR-018 | Validation errors must clearly identify which required data is missing | Specific field-level messaging |
| NFR-019 | Only valid next-status options must be presented to users | Context-sensitive UI controls |
| NFR-020 | Overdue tasks must be visually highlighted on the personal dashboard | Distinct visual treatment |
````

## 47. Retail Standard-365Retail/business-requirements.md #46

Score: 1.000

````text
| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-021 | The system must operate within the Azure DevOps platform ecosystem | Native Azure DevOps integration |
| NFR-022 | API access must enforce the same business rules as the user interface | Consistent rule enforcement |
| NFR-023 | The system must support standard authentication mechanisms used by the organization | Organizational SSO/identity provider |
````

## 48. Retail Standard-365Retail/business-requirements.md #47

Score: 1.000

````text
| Constraint ID | Constraint | Impact |
| --- | --- | --- |
| BC-001 | The solution must operate within the My Team organization boundary | All projects, documentation, and tasks are scoped to the My Team organization |
| BC-002 | Only registered team members may participate in project activities | User provisioning must precede project participation |
| BC-003 | Project ownership is mandatory and cannot be circumvented | System design must enforce ownership at all times; no orphaned projects are permitted |
| BC-004 | Documentation must follow organizational standards | Template structures are fixed and cannot be modified by individual users |
````

## 49. Retail Standard-365Retail/business-requirements.md #48

Score: 1.000

````text
| Constraint ID | Constraint | Impact |
| --- | --- | --- |
| BC-005 | The solution must be implemented within Azure DevOps | Technology stack and platform capabilities are bounded by Azure DevOps |
| BC-006 | Status transitions must follow defined valid paths | System cannot support ad-hoc or custom workflow paths outside defined transitions |
| BC-007 | Business rules must be enforced at the system level, not merely at the UI level | API-level enforcement is required to prevent circumvention |
| BC-008 | Version history must be immutable | Published BRD versions cannot be modified or deleted after publication |
````

## 50. Retail Standard-365Retail/business-requirements.md #49

Score: 1.000

````text
| Constraint ID | Constraint | Impact |
| --- | --- | --- |
| BC-009 | Projects must begin in "Not Started" status | No project may be created in an advanced lifecycle state |
| BC-010 | Tasks must begin in "To Do" status | No task may be created in an advanced state |
| BC-011 | BRDs must begin in "Draft" status at version 1.0 | No BRD may be created in "Published" status |
| BC-012 | A change summary is required for BRD version publication | Version increments cannot occur without documented rationale |
````

## 51. Retail Standard-365Retail/business-requirements.md #50

Score: 1.000

````text
| Constraint ID | Constraint | Impact |
| --- | --- | --- |
| BC-013 | Only project owners may add team members to projects | Team composition management is restricted to the owner role |
| BC-014 | Only task assignees or project owners may update task status | Status update permissions are narrowly scoped |
| BC-015 | Search results are bounded by project association | Users cannot discover or access BRDs in projects they are not associated with |
| BC-016 | Task assignees must be members currently associated with the project | Assignment validation must check current project membership |
````

## 52. Retail Standard-365Retail/business-requirements.md #51

Score: 1.000

````text
| Assumption ID | Assumption | Risk if Invalid |
| --- | --- | --- |
| AS-001 | The My Team organization has a defined roster of registered team members available for project assignment | Project creation and team association features would be non-functional without a user registry |
| AS-002 | Team members have appropriate access to the Azure DevOps platform | Users without platform access cannot utilize the solution |
| AS-003 | The organization has agreed upon the standardized BRD template structure (Executive Summary, Purpose & Scope, Business Objectives, Functional Requirements, Non-Functional Requirements) | Template disagreements would delay BRD creation feature delivery |
| AS-004 | Project ownership responsibilities are understood and accepted by team members who will serve as owners | Resistance to ownership accountability would undermine mandatory ownership enforcement |
````

## 53. Retail Standard-365Retail/business-requirements.md #52

Score: 1.000

````text
| Assumption ID | Assumption | Risk if Invalid |
| --- | --- | --- |
| AS-005 | The Azure DevOps platform supports the required customization for workflow enforcement and business rule implementation | Platform limitations could prevent full business rule enforcement |
| AS-006 | Full-text search capabilities are available or can be implemented within the platform to meet the 2-second response time requirement | Search functionality may require alternative implementation approaches |
| AS-007 | Real-time or near-real-time data refresh is supported for dashboard and status views | Users may experience stale data if refresh mechanisms are limited |
| AS-008 | The platform supports role-based access control at the project level to enforce access boundaries | Security requirements may require supplemental access control mechanisms |
````

## 54. Retail Standard-365Retail/business-requirements.md #53

Score: 1.000

````text
| Assumption ID | Assumption | Risk if Invalid |
| --- | --- | --- |
| AS-009 | The three-state project lifecycle (Not Started → In Progress → Completed) is sufficient for the organization's current needs | Additional states may be required, necessitating workflow redesign |
| AS-010 | The three-state task lifecycle (To Do → In Progress → Done) is sufficient for granular work tracking | Complex tasks may require intermediate states or sub-task capabilities |
| AS-011 | Draft/Published BRD statuses adequately represent the document lifecycle | Additional review or approval states may be needed in future iterations |
| AS-012 | A single project owner (rather than multiple owners or ownership groups) is the appropriate accountability model | Shared ownership needs would require role model changes |
````

## 55. Retail Standard-365Retail/business-requirements.md #54

Score: 1.000

````text
| Assumption ID | Assumption | Risk if Invalid |
| --- | --- | --- |
| AS-013 | Unique identifiers can be system-generated for projects and tasks without user input | Manual identifier assignment would add complexity to creation workflows |
| AS-014 | Version numbering follows a simple incremental model (1.0, 2.0, 3.0) | Complex versioning schemes (semantic versioning, branching) would require additional design |
| AS-015 | Historical audit data (timestamps, user identities for actions) can be captured and stored without significant performance impact | Audit logging overhead may require performance optimization |
````

## 56. Retail Standard-365Retail/business-requirements.md #55

Score: 1.000

````text
The following matrix provides complete traceability from functional requirements through user stories, BRD requirements, epics, and features. All nine (9) user stories are explicitly mapped.
````

## 57. Retail Standard-365Retail/business-requirements.md #56

Score: 1.000

````text
| FR ID | User Story ID | User Story Title | BRD Requirement Reference(s) | Epic | Feature | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR-001 | story-1 | Project creation to achieve structured project initialization with mandatory ownership | FR-001, FR-002, FR-011 | Project Management Solution for My Team | Project Lifecycle Management | High | Approved |
| FR-002 | story-2 | Project status transition to achieve accurate project lifecycle tracking | FR-003, FR-004, FR-014 | Project Management Solution for My Team | Project Lifecycle Management | High | Approved |
| FR-003 | story-3 | Team member association to achieve traceable project participation | FR-010, FR-013 | Project Management Solution for My Team | Project Lifecycle Management | High | Approved |
| FR-004 | story-4 | BRD creation to achieve standardized project documentation | FR-005, FR-015, FR-011 | Project Management Solution for My Team | BRD Creation and Document Management | High | Approved |
| FR-005 | story-5 | BRD editing and version management to achieve maintained documentation accuracy | FR-006, FR-013, FR-012 | Project Management Solution for My Team | BRD Creation and Document Management | High | Approved |
| FR-006 | story-6 | BRD search and retrieval to achieve efficient document discovery | FR-012, FR-006 | Project Management Solution for My Team | BRD Creation and Document Management | High | Approved |
| FR-007 | story-7 | Task creation and assignment to achieve granular work tracking within projects | FR-009, FR-007, FR-011 | Project Management Solution for My Team | Task Management and Team Collaboration | High | Approved |
| FR-008 | story-8 | Task status updates to achieve accurate progress tracking | FR-008, FR-009, FR-004, FR-014 | Project Management Solution for My Team | Task Management and Team Collaboration | High | Approved |
| FR-009 | story-9 | Personal task dashboard viewing to achieve consolidated work visibility across projects | FR-008, FR-009, FR-010 | Project Management Solution for My Team | Task Management and Team Collaboration | High | Approved |
````

## 58. Retail Standard-365Retail/business-requirements.md #57

Score: 1.000

````text
The following table demonstrates that all BRD functional requirements (FR-001 through FR-015) are addressed by at least one implementation-level functional requirement:
````

## 59. Retail Standard-365Retail/business-requirements.md #58

Score: 1.000

````text
| BRD Requirement | BRD Requirement Title | Covered By (Implementation FR) | Coverage Status |
| --- | --- | --- | --- |
| FR-001 | Project Creation | FR-001 | ✅ Covered |
| FR-002 | Mandatory Project Ownership Assignment | FR-001 | ✅ Covered |
| FR-003 | Project Lifecycle Status Management | FR-002 | ✅ Covered |
| FR-004 | Logical Status Transition Enforcement | FR-002, FR-008 | ✅ Covered |
| FR-005 | BRD Creation | FR-004 | ✅ Covered |
| FR-006 | BRD Management | FR-005, FR-006 | ✅ Covered |
| FR-007 | Project Activity Planning | FR-007 | ✅ Covered |
| FR-008 | Project Activity Tracking | FR-008, FR-009 | ✅ Covered |
| FR-009 | Task Tracking | FR-007, FR-008, FR-009 | ✅ Covered |
| FR-010 | Team Collaboration | FR-003, FR-009 | ✅ Covered |
| FR-011 | Minimum Data Completeness Enforcement | FR-001, FR-004, FR-007 | ✅ Covered |
| FR-012 | Project Documentation Organization | FR-005, FR-006 | ✅ Covered |
| FR-013 | Accountability and Traceability Support | FR-003, FR-005 | ✅ Covered |
| FR-014 | Workflow Integrity Enforcement | FR-002, FR-008 | ✅ Covered |
| FR-015 | Standardized Documentation Processes | FR-004 | ✅ Covered |
````

## 60. Retail Standard-365Retail/business-requirements.md #59

Score: 1.000

````text
| Feature | Associated User Stories | Story Count |
| --- | --- | --- |
| Project Lifecycle Management | story-1, story-2, story-3 | 3 |
| BRD Creation and Document Management | story-4, story-5, story-6 | 3 |
| Task Management and Team Collaboration | story-7, story-8, story-9 | 3 |
| Total | 9 | |
````

## 61. Retail Standard-365Retail/business-requirements.md #60

Score: 1.000

````text
![Diagram
````

## 62. Retail Standard-365Retail/business-requirements.md #61

Score: 1.000

````text
3](data:image/svg+xml;charset=utf-8;base64,PHN2ZyBpZD0ibWVybWFpZERpYWdyYW0iIHdpZHRoPSIyNzA5LjAxNTYyNSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iZmxvd2NoYXJ0IiBoZWlnaHQ9IjM3NCIgdmlld0JveD0iLTEyIC0xMiAyNzA5LjAxNTYyNSAzNzQiIHJvbGU9ImdyYXBoaWNzLWRvY3VtZW50IGRvY3VtZW50IiBhcmlhLXJvbGVkZXNjcmlwdGlvbj0iZmxvd2NoYXJ0LXYyIj48c3R5bGU+I21lcm1haWREaWFncmFte2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTZweDtmaWxsOiMzMzM7fUBrZXlmcmFtZXMgZWRnZS1hbmltYXRpb24tZnJhbWV7ZnJvbXtzdHJva2UtZGFzaG9mZnNldDowO319QGtleWZyYW1lcyBkYXNoe3Rve3N0cm9rZS1kYXNob2Zmc2V0OjA7fX0jbWVybWFpZERpYWdyYW0gLmVkZ2UtYW5pbWF0aW9uLXNsb3d7c3Ryb2tlLWRhc2hhcnJheTo5LDUhaW1wb3J0YW50O3N0cm9rZS1kYXNob2Zmc2V0OjkwMDthbmltYXRpb246ZGFzaCA1MHMgbGluZWFyIGluZmluaXRlO3N0cm9rZS1saW5lY2FwOnJvdW5kO30jbWVybWFpZERpYWdyYW0gLmVkZ2UtYW5pbWF0aW9uLWZhc3R7c3Ryb2tlLWRhc2hhcnJheTo5LDUhaW1wb3J0YW50O3N0cm9rZS1kYXNob2Zmc2V0OjkwMDthbmltYXRpb246ZGFzaCAyMHMgbGluZWFyIGluZmluaXRlO3N0cm9rZS1saW5lY2FwOnJvdW5kO30jbWVybWFpZERpYWdyYW0gLmVycm9yLWljb257ZmlsbDojNTUyMjIyO30jbWVybWFpZERpYWdyYW0gLmVycm9yLXRleHR7ZmlsbDojNTUyMjIyO3N0cm9rZTojNTUyMjIyO30jbWVybWFpZERpYWdyYW0gLmVkZ2UtdGhpY2tuZXNzLW5vcm1hbHtzdHJva2Utd2lkdGg6MXB4O30jbWVybWFpZERpYWdyYW0gLmVkZ2UtdGhpY2tuZXNzLXRoaWNre3N0cm9rZS13aWR0aDozLjVweDt9I21lcm1haWREaWFncmFtIC5lZGdlLXBhdHRlcm4tc29saWR7c3Ryb2tlLWRhc2hhcnJheTowO30jbWVybWFpZERpYWdyYW0gLmVkZ2UtdGhpY2tuZXNzLWludmlzaWJsZXtzdHJva2Utd2lkdGg6MDtmaWxsOm5vbmU7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS1wYXR0ZXJuLWRhc2hlZHtzdHJva2UtZGFzaGFycmF5OjM7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZS1wYXR0ZXJuLWRvdHRlZHtzdHJva2UtZGFzaGFycmF5OjI7fSNtZXJtYWlkRGlhZ3JhbSAubWFya2Vye2ZpbGw6IzMzMzMzMztzdHJva2U6IzMzMzMzMzt9I21lcm1haWREaWFncmFtIC5tYXJrZXIuY3Jvc3N7c3Ryb2tlOiMzMzMzMzM7fSNtZXJtYWlkRGlhZ3JhbSBzdmd7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O30jbWVybWFpZERpYWdyYW0gcHttYXJnaW46MDt9I21lcm1haWREaWFncmFtIC5sYWJlbHtmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Y29sb3I6IzMzMzt9I21lcm1haWREaWFncmFtIC5jbHVzdGVyLWxhYmVsIHRleHR7ZmlsbDojMzMzO30jbWVybWFpZERpYWdyYW0gLmNsdXN0ZXItbGFiZWwgc3Bhbntjb2xvcjojMzMzO30jbWVybWFpZERpYWdyYW0gLmNsdXN0ZXItbGFiZWwgc3BhbiBwe2JhY2tncm91bmQtY29sb3I6dHJhbnNwYXJlbnQ7fSNtZXJtYWlkRGlhZ3JhbSAubGFiZWwgdGV4dCwjbWVybWFpZERpYWdyYW0gc3BhbntmaWxsOiMzMzM7Y29sb3I6IzMzMzt9I21lcm1haWREaWFncmFtIC5ub2RlIHJlY3QsI21lcm1haWREaWFncmFtIC5ub2RlIGNpcmNsZSwjbWVybWFpZERpYWdyYW0gLm5vZGUgZWxsaXBzZSwjbWVybWFpZERpYWdyYW0gLm5vZGUgcG9seWdvbiwjbWVybWFpZERpYWdyYW0gLm5vZGUgcGF0aHtmaWxsOiNFQ0VDRkY7c3Ryb2tlOiM5MzcwREI7c3Ryb2tlLXdpZHRoOjFweDt9I21lcm1haWREaWFncmFtIC5yb3VnaC1ub2RlIC5sYWJlbCB0ZXh0LCNtZXJtYWlkRGlhZ3JhbSAubm9kZSAubGFiZWwgdGV4dCwjbWVybWFpZERpYWdyYW0gLmltYWdlLXNoYXBlIC5sYWJlbCwjbWVybWFpZERpYWdyYW0gLmljb24tc2hhcGUgLmxhYmVse3RleHQtYW5jaG9yOm1pZGRsZTt9I21lcm1haWREaWFncmFtIC5ub2RlIC5rYXRleCBwYXRoe2ZpbGw6IzAwMDtzdHJva2U6IzAwMDtzdHJva2Utd2lkdGg6MXB4O30jbWVybWFpZERpYWdyYW0gLnJvdWdoLW5vZGUgLmxhYmVsLCNtZXJtYWlkRGlhZ3JhbSAubm9kZSAubGFiZWwsI21lcm1haWREaWFncmFtIC5pbWFnZS1zaGFwZSAubGFiZWwsI21lcm1haWREaWFncmFtIC5pY29uLXNoYXBlIC5sYWJlbHt0ZXh0LWFsaWduOmNlbnRlcjt9I21lcm1haWREaWFncmFtIC5ub2RlLmNsaWNrYWJsZXtjdXJzb3I6cG9pbnRlcjt9I21lcm1haWREaWFncmFtIC5yb290IC5hbmNob3IgcGF0aHtmaWxsOiMzMzMzMzMhaW1wb3J0YW50O3N0cm9rZS13aWR0aDowO3N0cm9rZTojMzMzMzMzO30jbWVybWFpZERpYWdyYW0gLmFycm93aGVhZFBhdGh7ZmlsbDojMzMzMzMzO30jbWVybWFpZERpYWdyYW0gLmVkZ2VQYXRoIC5wYXRoe3N0cm9rZTojMzMzMzMzO3N0cm9rZS13aWR0aDoyLjBweDt9I21lcm1haWREaWFncmFtIC5mbG93Y2hhcnQtbGlua3tzdHJva2U6IzMzMzMzMztmaWxsOm5vbmU7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZUxhYmVse2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt0ZXh0LWFsaWduOmNlbnRlcjt9I21lcm1haWREaWFncmFtIC5lZGdlTGFiZWwgcHtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNtZXJtYWlkRGlhZ3JhbSAuZWRnZUxhYmVsIHJlY3R7b3BhY2l0eTowLjU7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO2ZpbGw6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt9I21lcm1haWREaWFncmFtIC5sYWJlbEJrZ3tiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLCAyMzIsIDIzMiwgMC41KTt9I21lcm1haWREaWFncmFtIC5jbHVzdGVyIHJlY3R7ZmlsbDojZmZmZmRlO3N0cm9rZTojYWFhYTMzO3N0cm9rZS13aWR0aDoxcHg7fSNtZXJtYWlkRGlhZ3JhbSAuY2x1c3RlciB0ZXh0e2ZpbGw6IzMzMzt9I21lcm1haWREaWFncmFtIC5jbHVzdGVyIHNwYW57Y29sb3I6IzMzMzt9I21lcm1haWREaWFncmFtIGRpdi5tZXJtYWlkVG9vbHRpcHtwb3NpdGlvbjphYnNvbHV0ZTt0ZXh0LWFsaWduOmNlbnRlcjttYXgtd2lkdGg6MjAwcHg7cGFkZGluZzoycHg7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxMnB4O2JhY2tncm91bmQ6aHNsKDgwLCAxMDAlLCA5Ni4yNzQ1MDk4MDM5JSk7Ym9yZGVyOjFweCBzb2xpZCAjYWFhYTMzO2JvcmRlci1yYWRpdXM6MnB4O3BvaW50ZXItZXZlbnRzOm5vbmU7ei1pbmRleDoxMDA7fSNtZXJtYWlkRGlhZ3JhbSAuZmxvd2NoYXJ0VGl0bGVUZXh0e3RleHQtYW5jaG9yOm1pZGRsZTtmb250LXNpemU6MThweDtmaWxsOiMzMzM7fSNtZXJtYWlkRGlhZ3JhbSByZWN0LnRleHR7ZmlsbDpub25lO3N0cm9rZS13aWR0aDowO30jbWVybWFpZERpYWdyYW0gLmljb24tc2hhcGUsI21lcm1haWREaWFncmFtIC5pbWFnZS1zaGFwZXtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7dGV4dC1hbGlnbjpjZW50ZXI7fSNtZXJtYWlkRGlhZ3JhbSAuaWNvbi1zaGFwZSBwLCNtZXJtYWlkRGlhZ3JhbSAuaW1hZ2Utc2hhcGUgcHtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7cGFkZGluZzoycHg7fSNtZXJtYWlkRGlhZ3JhbSAuaWNvbi1zaGFwZSByZWN0LCNtZXJtYWlkRGlhZ3JhbSAuaW1hZ2Utc2hhcGUgcmVjdHtvcGFjaXR5OjAuNTtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7ZmlsbDpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO30jbWVybWFpZERpYWdyYW0gLmxhYmVsLWljb257ZGlzcGxheTppbmxpbmUtYmxvY2s7aGVpZ2h0OjFlbTtvdmVyZmxvdzp2aXNpYmxlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO30jbWVybWFpZERpYWdyYW0gLm5vZGUgLmxhYmVsLWljb24gcGF0aHtmaWxsOmN1cnJlbnRDb2xvcjtzdHJva2U6cmV2ZXJ0O3N0cm9rZS13aWR0aDpyZXZlcnQ7fSNtZXJtYWlkRGlhZ3JhbSA6cm9vdHstLW1lcm1haWQtZm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO308L3N0eWxlPjxnPjxtYXJrZXIgaWQ9Im1lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iNSIgcmVmWT0iNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI4IiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMCAwIEwgMTAgNSBMIDAgMTAgeiIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRTdGFydCIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iNC41IiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjgiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAwIDUgTCAxMCAxMCBMIDEwIDAgeiIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItY2lyY2xlRW5kIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSIxMSIgcmVmWT0iNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTEiIG1hcmtlckhlaWdodD0iMTEiIG9yaWVudD0iYXV0byI+PGNpcmNsZSBjeD0iNSIgY3k9IjUiIHI9IjUiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ij48L2NpcmNsZT48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItY2lyY2xlU3RhcnQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9Ii0xIiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VySGVpZ2h0PSIxMSIgb3JpZW50PSJhdXRvIj48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iNSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiPjwvY2lyY2xlPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1jcm9zc0VuZCIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMSAxMSIgcmVmWD0iMTIiIHJlZlk9IjUuMiIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTEiIG1hcmtlckhlaWdodD0iMTEiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAxLDEgbCA5LDkgTSAxMCwxIGwgLTksOSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMjsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItY3Jvc3NTdGFydCIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMSAxMSIgcmVmWD0iLTEiIHJlZlk9IjUuMiIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTEiIG1hcmtlckhlaWdodD0iMTEiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAxLDEgbCA5LDkgTSAxMCwxIGwgLTksOSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMjsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiPjwvcGF0aD48L21hcmtlcj48ZyBjbGFzcz0icm9vdCI+PGcgY2xhc3M9ImNsdXN0ZXJzIj48L2c+PGcgY2xhc3M9ImVkZ2VQYXRocyI+PHBhdGggZD0iTTExNzcuMDE2LDU2LjM4NUwxMDUwLjkzMiw2NS40ODhDOTI0Ljg0OSw3NC41OSw2NzIuNjgyLDkyLjc5NSw1NDYuNTk5LDEwNS4zOThDNDIwLjUxNiwxMTgsNDIwLjUxNiwxMjUsNDIwLjUxNiwxMjguNUw0MjAuNTE2LDEzMiIgaWQ9IkxfRV9GMV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9FX0YxXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1URTNOeTR3TVRVMk1qVXNJbmtpT2pVMkxqTTROVEl5TWpjNE5qSXpPREF5ZlN4N0luZ2lPalF5TUM0MU1UVTJNalVzSW5raU9qRXhNWDBzZXlKNElqbzBNakF1TlRFMU5qSTFMQ0o1SWpveE16WjlYUT09IiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMTMwNy4wMTYsODZMMTMwNy4wMTYsOTAuMTY3QzEzMDcuMDE2LDk0LjMzMywxMzA3LjAxNiwxMDIuNjY3LDEzMDcuMDE2LDExMC4zMzNDMTMwNy4wMTYsMTE4LDEzMDcuMDE2LDEyNSwxMzA3LjAxNiwxMjguNUwxMzA3LjAxNiwxMzIiIGlkPSJMX0VfRjJfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfRV9GMl8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNVE13Tnk0d01UVTJNalVzSW5raU9qZzJmU3g3SW5naU9qRXpNRGN1TURFMU5qSTFMQ0o1SWpveE1URjlMSHNpZUNJNk1UTXdOeTR3TVRVMk1qVXNJbmtpT2pFek5uMWQiIG1hcmtlci1lbmQ9InVybCgjbWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSI+PC9wYXRoPjxwYXRoIGQ9Ik0xNDM3LjAxNiw1NS45NDZMMTU3MC4zNDksNjUuMTIyQzE3MDMuNjgyLDc0LjI5NywxOTcwLjM0OSw5Mi42NDksMjEwMy42ODIsMTA1LjMyNEMyMjM3LjAxNiwxMTgsMjIzNy4wMTYsMTI1LDIyMzcuMDE2LDEyOC41TDIyMzcuMDE2LDEzMiIgaWQ9IkxfRV9GM18wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9FX0YzXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UUXpOeTR3TVRVMk1qVXNJbmtpT2pVMUxqazBOakl6TmpVMU9URXpPVGM0Tkgwc2V5SjRJam95TWpNM0xqQXhOVFl5TlN3aWVTSTZNVEV4ZlN4N0luZ2lPakl5TXpjdU1ERTFOakkxTENKNUlqb3hNelo5WFE9PSIgbWFya2VyLWVuZD0idXJsKCNtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIj48L3BhdGg+PHBhdGggZD0iTTI5MC41MTYsMjAzLjA4NEwyNjIuODA2LDIwOS4wN0MyMzUuMDk2LDIxNS4wNTYsMTc5LjY3NywyMjcuMDI4LDE1MS45NjcsMjM4LjUxNEMxMjQuMjU4LDI1MCwxMjQuMjU4LDI2MSwxMjQuMjU4LDI2Ni41TDEyNC4yNTgsMjcyIiBpZD0iTF9GMV9TMV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9GMV9TMV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNamt3TGpVeE5UWXlOU3dpZVNJNk1qQXpMakE0TXpZME56VTRNekV6TXpNM2ZTeDdJbmdpT2pFeU5DNHlOVGM0TVRJMUxDSjVJam95TXpsOUxIc2llQ0k2TVRJMExqSTFOemd4TWpVc0lua2lPakkzTm4xZCIgbWFya2VyLWVuZD0idXJsKCNtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIj48L3BhdGg+PHBhdGggZD0iTTQyMC41MTYsMjE0TDQyMC41MTYsMjE4LjE2N0M0MjAuNTE2LDIyMi4zMzMsNDIwLjUxNiwyMzAuNjY3LDQyMC41MTYsMjM4LjMzM0M0MjAuNTE2LDI0Niw0MjAuNTE2LDI1Myw0MjAuNTE2LDI1Ni41TDQyMC41MTYsMjYwIiBpZD0iTF9GMV9TMl8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9GMV9TMl8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZOREl3TGpVeE5UWXlOU3dpZVNJNk1qRTBmU3g3SW5naU9qUXlNQzQxTVRVMk1qVXNJbmtpT2pJek9YMHNleUo0SWpvME1qQXVOVEUxTmpJMUxDSjVJam95TmpSOVhRPT0iIG1hcmtlci1lbmQ9InVybCgjbWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSI+PC9wYXRoPjxwYXRoIGQ9Ik01NTAuNTE2LDIwMS44MzlMNTgwLjUxNiwyMDguMDMyQzYxMC41MTYsMjE0LjIyNiw2NzAuNTE2LDIyNi42MTMsNzAwLjUxNiwyMzYuMzA2QzczMC41MTYsMjQ2LDczMC41MTYsMjUzLDczMC41MTYsMjU2LjVMNzMwLjUxNiwyNjAiIGlkPSJMX0YxX1MzXzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0YxX1MzXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk5UVXdMalV4TlRZeU5Td2llU0k2TWpBeExqZ3pPRGN3T1RZM056UXhPVE0yZlN4N0luZ2lPamN6TUM0MU1UVTJNalVzSW5raU9qSXpPWDBzZXlKNElqbzNNekF1TlRFMU5qSTFMQ0o1SWpveU5qUjlYUT09IiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMTE3Ny4wMTYsMjAzLjg2NEwxMTUwLjY0MSwyMDkuNzJDMTEyNC4yNjYsMjE1LjU3NiwxMDcxLjUxNiwyMjcuMjg4LDEwNDUuMTQxLDIzOC42NDRDMTAxOC43NjYsMjUwLDEwMTguNzY2LDI2MSwxMDE4Ljc2NiwyNjYuNUwxMDE4Ljc2NiwyNzIiIGlkPSJMX0YyX1M0XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0YyX1M0XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1URTNOeTR3TVRVMk1qVXNJbmtpT2pJd015NDROak00TXpNME56YzRPRE00ZlN4N0luZ2lPakV3TVRndU56WTFOakkxTENKNUlqb3lNemw5TEhzaWVDSTZNVEF4T0M0M05qVTJNalVzSW5raU9qSTNObjFkIiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMTMwNy4wMTYsMjE0TDEzMDcuMDE2LDIxOC4xNjdDMTMwNy4wMTYsMjIyLjMzMywxMzA3LjAxNiwyMzAuNjY3LDEzMDcuMDE2LDIzOC4zMzNDMTMwNy4wMTYsMjQ2LDEzMDcuMDE2LDI1MywxMzA3LjAxNiwyNTYuNUwxMzA3LjAxNiwyNjAiIGlkPSJMX0YyX1M1XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0YyX1M1XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UTXdOeTR3TVRVMk1qVXNJbmtpT2pJeE5IMHNleUo0SWpveE16QTNMakF4TlRZeU5Td2llU0k2TWpNNWZTeDdJbmdpT2pFek1EY3VNREUxTmpJMUxDSjVJam95TmpSOVhRPT0iIG1hcmtlci1lbmQ9InVybCgjbWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSI+PC9wYXRoPjxwYXRoIGQ9Ik0xNDM3LjAxNiwyMDEuODM5TDE0NjcuMDE2LDIwOC4wMzJDMTQ5Ny4wMTYsMjE0LjIyNiwxNTU3LjAxNiwyMjYuNjEzLDE1ODcuMDE2LDIzNi4zMDZDMTYxNy4wMTYsMjQ2LDE2MTcuMDE2LDI1MywxNjE3LjAxNiwyNTYuNUwxNjE3LjAxNiwyNjAiIGlkPSJMX0YyX1M2XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0YyX1M2XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UUXpOeTR3TVRVMk1qVXNJbmtpT2pJd01TNDRNemczTURrMk56YzBNVGt6Tm4wc2V5SjRJam94TmpFM0xqQXhOVFl5TlN3aWVTSTZNak01ZlN4N0luZ2lPakUyTVRjdU1ERTFOakkxTENKNUlqb3lOalI5WFE9PSIgbWFya2VyLWVuZD0idXJsKCNtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIj48L3BhdGg+PHBhdGggZD0iTTIxMDcuMDE2LDIwMS44MzlMMjA3Ny4wMTYsMjA4LjAzMkMyMDQ3LjAxNiwyMTQuMjI2LDE5ODcuMDE2LDIyNi42MTMsMTk1Ny4wMTYsMjM2LjMwNkMxOTI3LjAxNiwyNDYsMTkyNy4wMTYsMjUzLDE5MjcuMDE2LDI1Ni41TDE5MjcuMDE2LDI2MCIgaWQ9IkxfRjNfUzdfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfRjNfUzdfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TWpFd055NHdNVFUyTWpVc0lua2lPakl3TVM0NE16ZzNNRGsyTnpjME1Ua3pObjBzZXlKNElqb3hPVEkzTGpBeE5UWXlOU3dpZVNJNk1qTTVmU3g3SW5naU9qRTVNamN1TURFMU5qSTFMQ0o1SWpveU5qUjlYUT09IiBtYXJrZXItZW5kPSJ1cmwoI21lcm1haWREaWFncmFtX2Zsb3djaGFydC12Mi1wb2ludEVuZCkiPjwvcGF0aD48cGF0aCBkPSJNMjIzNy4wMTYsMjE0TDIyMzcuMDE2LDIxOC4xNjdDMjIzNy4wMTYsMjIyLjMzMywyMjM3LjAxNiwyMzAuNjY3LDIyMzcuMDE2LDIzOC4zMzNDMjIzNy4wMTYsMjQ2LDIyMzcuMDE2LDI1MywyMjM3LjAxNiwyNTYuNUwyMjM3LjAxNiwyNjAiIGlkPSJMX0YzX1M4XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0YzX1M4XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1qSXpOeTR3TVRVMk1qVXNJbmtpT2pJeE5IMHNleUo0SWpveU1qTTNMakF4TlRZeU5Td2llU0k2TWpNNWZTeDdJbmdpT2pJeU16Y3VNREUxTmpJMUxDSjVJam95TmpSOVhRPT0iIG1hcmtlci1lbmQ9InVybCgjbWVybWFpZERpYWdyYW1fZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSI+PC9wYXRoPjxwYXRoIGQ9Ik0yMzY3LjAxNiwyMDEuODM5TDIzOTcuMDE2LDIwOC4wMzJDMjQyNy4wMTYsMjE0LjIyNiwyNDg3LjAxNiwyMjYuNjEzLDI1MTcuMDE2LDIzNi4zMDZDMjU0Ny4wMTYsMjQ2LDI1NDcuMDE2LDI1MywyNTQ3LjAxNiwyNTYuNUwyNTQ3LjAxNiwyNjAiIGlkPSJMX0YzX1M5XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX0YzX1M5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1qTTJOeTR3TVRVMk1qVXNJbmtpT2pJd01TNDRNemczTURrMk56YzBNVGt6Tm4wc2V5SjRJam95TlRRM0xqQXhOVFl5TlN3aWVTSTZNak01ZlN4N0luZ2lPakkxTkRjdU1ERTFOakkxTENKNUlqb3lOalI5WFE9PSIgbWFya2VyLWVuZD0idXJsKCNtZXJtYWlkRGlhZ3JhbV9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIj48L3BhdGg+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWxzIj48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfRV9GMV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfRV9GMl8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfRV9GM18wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfRjFfUzFfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwgIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX0YxX1MyXzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9GMV9TM18wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfRjJfUzRfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwgIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX0YyX1M1XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9GMl9TNl8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfRjNfUzdfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwgIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX0YzX1M4XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9GM19TOV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PGcgY2xhc3M9Im5vZGVzIj48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtRS0wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMzA3LjAxNTYyNSwgNDcpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItMzkiIHdpZHRoPSIyNjAiIGhlaWdodD0iNzgiPjwvcmVjdD48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAsIC0yNCkiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPkVwaWM6IFByb2plY3QgTWFuYWdlbWVudCBTb2x1dGlvbiBmb3IgTXkgVGVhbTwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LUYxLTIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQyMC41MTU2MjUsIDE3NSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii0xMzAiIHk9Ii0zOSIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI3OCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEwMCwgLTI0KSI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IHdpZHRoPSIyMDAiIGhlaWdodD0iNDgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZTsgd2hpdGUtc3BhY2U6IGJyZWFrLXNwYWNlczsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyB3aWR0aDogMjAwcHg7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+RmVhdHVyZTogUHJvamVjdCBMaWZlY3ljbGUgTWFuYWdlbWVudDwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LUYyLTQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEzMDcuMDE1NjI1LCAxNzUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItMzkiIHdpZHRoPSIyNjAiIGhlaWdodD0iNzgiPjwvcmVjdD48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAsIC0yNCkiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPkZlYXR1cmU6IEJSRCBDcmVhdGlvbiBhbmQgRG9jdW1lbnQgTWFuYWdlbWVudDwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LUYzLTYiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIyMzcuMDE1NjI1LCAxNzUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItMzkiIHdpZHRoPSIyNjAiIGhlaWdodD0iNzgiPjwvcmVjdD48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAsIC0yNCkiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPkZlYXR1cmU6IFRhc2sgTWFuYWdlbWVudCBhbmQgVGVhbSBDb2xsYWJvcmF0aW9uPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtUzEtOCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTI0LjI1NzgxMjUsIDMwMykiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii0xMTYuMjU3ODEyNSIgeT0iLTI3IiB3aWR0aD0iMjMyLjUxNTYyNSIgaGVpZ2h0PSI1NCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTg2LjI1NzgxMjUsIC0xMikiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMTcyLjUxNTYyNSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD5zdG9yeS0xOiBQcm9qZWN0IENyZWF0aW9uPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtUzItMTAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQyMC41MTU2MjUsIDMwMykiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii0xMzAiIHk9Ii0zOSIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI3OCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEwMCwgLTI0KSI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IHdpZHRoPSIyMDAiIGhlaWdodD0iNDgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZTsgd2hpdGUtc3BhY2U6IGJyZWFrLXNwYWNlczsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyB3aWR0aDogMjAwcHg7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+c3RvcnktMjogUHJvamVjdCBTdGF0dXMgVHJhbnNpdGlvbjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LVMzLTEyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg3MzAuNTE1NjI1LCAzMDMpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItMzkiIHdpZHRoPSIyNjAiIGhlaWdodD0iNzgiPjwvcmVjdD48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAsIC0yNCkiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPnN0b3J5LTM6IFRlYW0gTWVtYmVyIEFzc29jaWF0aW9uPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtUzQtMTQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwMTguNzY1NjI1LCAzMDMpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTA4LjI1IiB5PSItMjciIHdpZHRoPSIyMTYuNSIgaGVpZ2h0PSI1NCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTc4LjI1LCAtMTIpIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjE1Ni41IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPnN0b3J5LTQ6IEJSRCBDcmVhdGlvbjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LVM1LTE2IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMzA3LjAxNTYyNSwgMzAzKSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTEzMCIgeT0iLTM5IiB3aWR0aD0iMjYwIiBoZWlnaHQ9Ijc4Ij48L3JlY3Q+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTAwLCAtMjQpIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI0OCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD5zdG9yeS01OiBCUkQgRWRpdGluZyBhbmQgVmVyc2lvbiBNYW5hZ2VtZW50PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtUzYtMTgiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MTcuMDE1NjI1LCAzMDMpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItMzkiIHdpZHRoPSIyNjAiIGhlaWdodD0iNzgiPjwvcmVjdD48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAsIC0yNCkiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPnN0b3J5LTY6IEJSRCBTZWFyY2ggYW5kIFJldHJpZXZhbDwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LVM3LTIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxOTI3LjAxNTYyNSwgMzAzKSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTEzMCIgeT0iLTM5IiB3aWR0aD0iMjYwIiBoZWlnaHQ9Ijc4Ij48L3JlY3Q+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTAwLCAtMjQpIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI0OCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD5zdG9yeS03OiBUYXNrIENyZWF0aW9uIGFuZCBBc3NpZ25tZW50PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtUzgtMjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIyMzcuMDE1NjI1LCAzMDMpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItMzkiIHdpZHRoPSIyNjAiIGhlaWdodD0iNzgiPjwvcmVjdD48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAsIC0yNCkiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPnN0b3J5LTg6IFRhc2sgU3RhdHVzIFVwZGF0ZXM8L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1TOS0yNCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjU0Ny4wMTU2MjUsIDMwMykiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii0xMzAiIHk9Ii0zOSIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI3OCI+PC9yZWN0PjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEwMCwgLTI0KSI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IHdpZHRoPSIyMDAiIGhlaWdodD0iNDgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZTsgd2hpdGUtc3BhY2U6IGJyZWFrLXNwYWNlczsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyB3aWR0aDogMjAwcHg7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+c3RvcnktOTogUGVyc29uYWwgVGFzayBEYXNoYm9hcmQ8L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjwvZz48L2c+PC9nPjwvc3ZnPg==)
````

## 63. Retail Standard-365Retail/business-requirements.md #62

Score: 1.000

````text
Several BRD requirements represent cross-cutting concerns that are addressed by multiple implementation-level functional requirements:
````

## 64. Retail Standard-365Retail/business-requirements.md #63

Score: 1.000

````text
| Cross-Cutting Concern | BRD Requirement | Implementation FRs Addressing This Concern |
| --- | --- | --- |
| Mandatory Data Completeness | FR-011 | FR-001 (Project), FR-004 (BRD), FR-007 (Task) |
| Workflow Integrity | FR-014 | FR-002 (Project Status), FR-008 (Task Status) |
| Accountability and Traceability | FR-013 | FR-003 (Team Association), FR-005 (Version History) |
| Logical Status Transitions | FR-004 | FR-002 (Project Transitions), FR-008 (Task Transitions) |
| Documentation Organization | FR-012 | FR-005 (Version Management), FR-006 (Search/Retrieval) |
````

## 65. Retail Standard-365Retail/business-requirements.md #64

Score: 1.000

````text
| Term | Definition |
| --- | --- |
| BRD | Business Requirements Document – a standardized document capturing business requirements for a project |
| Project Owner | The designated team member accountable for a project's delivery and team composition |
| Status Transition | The act of moving a project or task from one lifecycle state to another |
| Version History | The chronological record of all published versions of a BRD |
| Team Member Association | The formal linkage between a registered team member and a specific project |
| Personal Dashboard | A consolidated view of all tasks assigned to an individual across all projects |
| Draft | The initial or working status of a BRD that has not yet been formally published |
| Published | The status of a BRD version that has been formally released and is immutable |
````

## 66. Retail Standard-365Retail/business-requirements.md #65

Score: 1.000

````text
| Role | Name | Date | Signature |
| --- | --- | --- | --- |
| Business Owner | ___________________ | __________ | __________ |
| Project Sponsor | ___________________ | __________ | __________ |
| Technical Lead | ___________________ | __________ | __________ |
| QA Lead | ___________________ | __________ | __________ |
````

## 67. Retail Standard-365Retail/business-requirements.md #66

Score: 1.000

````text
*End of Document*
````

## 68. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #0

Score: 1.000

````text
365 Retail compliance, regulatory, or governance guidelines
````

## 69. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #1

Score: 1.000

````text
1.1 365 Information Security Policy (master reference)
* Document: 365 Information Security Policy 02072025.pdf
https://365retailmarkets.atlassian.net/wiki/pages/viewpageattachments.action?pageId=3652386874&preview=%2F3652386874%2F5583405070%2F365+Information+Security+Policy+02072025.pdf
Key principles:
* Scope
o Applies to all 365 entities, platforms, subsidiaries, employees, contractors, and systems.
o Covers all sensitive data: PHI, PII, PCI, Confidential Information (CI), Cardholder Data (CHD), etc.
* Policy baseline
o All information (written, spoken, electronic, printed) must be protected against unauthorized modification, destruction, or disclosure throughout its life cycle.
o Policies and procedures must be:
* Documented
* Available to responsible individuals
* Retained for at least 5 years
* Periodically reviewed and updated
* Roles & responsibilities
o Information Security Team (IST):
* Maintains policies, supports systems, educates users, performs audits.
* Ensures compliance with laws including GDPR, CCPA, CPRA, FCRA, HIPAA, BIPA, GLBA, etc.
o Information Owners, Custodians, Users: clear duties around classification, access, correct use, and reporting incidents.
* Information classification
o Data must be classified by sensitivity (e.g., PHI, PII, PCI, CI, Internal).
o Same classification applies across all formats (source, DB, report, export).
* Data integrity & secure transmission
o Integrity controls: audits, RAID, ECC, checksums, encryption, digital signatures.
o Transmission:
* Sensitive data must use secure protocols (TLS, SSL, IPsec, SFTP).
* Prohibits sending sensitive data via unencrypted email/SMS/IM.
* Requires secure external file sharing (encrypted links, password protected files, etc.).
* Audit and lifecycle governance
o Systems audit   IST performs yearly audits of systems that store/process PHI, PII, PCI, CI or internal info. Non compliance is tracked via change management.
o Policy audit   policy itself is reviewed yearly; changes tracked in Document Revisions.
There is also a Confluence rendering of this titled  Security policy (from 365) :
Security policy (from 365)
````

## 70. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #2

Score: 1.000

````text
2.1 Privacy governance program (GDPR & beyond)
* Page: SOS 47951   International and US Privacy Law Governance Program (GDPR)
SOS-47951 International and US Privacy Law Governance Program (GDPR)
Scope & expectations:
* Build a formal privacy law governance program across:
o Phase 1   GDPR: 365pay, V5 kiosks, MM6, PicoCooler, PicoMarket, Stockwell, ADM.
o Phase 2   LATAM (Parlevel products).
o Phase 3   CCPA/CPRA/other US laws.
* Activities:
o Review existing data privacy practices and Privacy Notice for compliance.
o Complete Data Protection Impact Assessments (DPIAs) for EU sold products.
o Implement:
* Data Protection by Design (DPbD)
* Privacy by Default
in the product development lifecycle.
Implications for your work:
* New or changed features on in scope products may require:
o DPIA review/updates if they change data flows, data types, or risk.
o Evidence of DPbD/Privacy by Default in requirements and design (data minimization, access controls, retention, etc.).
````

## 71. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #3

Score: 1.000

````text
3.1 Secure Development Lifecycle
* Page: 365 Secure Development Lifecycle
365 Secure Development Lifecycle
The SDLC page (and the Information Security Policy) jointly require:
* Embedding security and privacy controls at:
o Requirements ? Design ? Implementation ? Verification ? Release ? Response.
* Using change management:
o Significant changes are tracked as Epics.
o Audit, pen tests, vulnerability remediation integrate into the lifecycle.
When you document a project or feature, you should be able to show:
* Where security/privacy requirements are defined.
* How they are tested/verified (functional tests, pen tests, privacy tests).
* How changes are approved (CAB) and released.
````

## 72. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #4

Score: 1.000

````text
4.1 Internal systems & policy audits
From the security policy (Confluence view):
Security policy (from 365)
* Systems Audit (annual)   checks:
o Systems processing PHI/PII/PCI/CI against the 365 policy.
o Non compliant items ? documented, tracked, remediated via change management.
* Policy Audit (annual)   ensures:
o Policy remains aligned with best practices and regulatory changes.
4.2 Customer / vendor audits (example)
* Jira: Compass Vendor Security Audit (ISEC 711)
ISEC-711: Compass Vendor Security AuditDone
Focus areas (typical large client audit expectations):
* IT security policies, risk management, user privilege management.
* Change management, secure configuration, malware protection, monitoring.
* Incident management, business continuity & disaster recovery.
* Data protection, privacy, and POS operations (including valid PCI DSS Attestations of Compliance, SOC reports, etc.).
Use this as a reference for what enterprise customers expect you to demonstrate.
````

## 73. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #5

Score: 1.000

````text
Depending on what you re doing, here s how to use these guidelines:
````

## 74. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #6

Score: 1.000

````text
o Add a  Compliance & Governance  section with bullets like:
*  Subject to 365 Information Security Policy and SDLC. 
*  Check if change requires DPIA update under SOS 47951. 
*  Ensure PCI/PII handling follows encryption and transmission requirements.
````

## 75. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #7

Score: 1.000

````text
o Explicitly call out:
* Data collected, stored, transmitted, and classification (PII, PCI, etc.).
* Where encryption at rest/in transit applies.
* Retention and access control model.
````

## 76. Retail Standard-365Retail/Compliance/365 Retail Compliance, regulatory and Governance guidelines.txt #8

Score: 1.000

````text
o For any new integration or process, ensure:
* There s a clear owner (Information Owner).
* Auditability: logs, reports, and documentation kept at least 5 years.
* Alignment with privacy governance (GDPR/US) if it touches end user data.
````

## 77. Retail Standard-365Retail/Design/Coding+Checklists.txt #0

Score: 1.000

````text
Coding Checklists
Also see, Screen-shared Recording that goes through the checklists.
Checklists before Pull Request Creation
Java Development Checklist
* Use JavaDoc when necessary
* Avoid using boolean parameters in method 
* Minimize the accessibility of classes and member 
* Understand logging with SLF4J [Use parameterized messages]
* Check for the usage of String concatenation in log output statement (Java) 
o security logging (don t log credentials or mask credential in output)
o unnecessary logging (don t log object lists or dev debugging log output as info level)
Git Commit Checklist
* Follow development checklist
* SpotBugs for Java/Kotlin, ESLint for JavaScript/TypeScript
* Reformat code (at least match the surrounding code style)
* Check database query performance
* Test and verify your changes
o Write unit/integration tests and use ./gradlew build for Java/Kotlin
* View commit diff: review changes to not include extra changes, fix typos, improve comments etc.
* Write meaningful commit message in this format
Dev Complete Checklist
* Build works locally (e.g. ./gradlew build) 
* Write tests and test your changes (locally or in test environment) 
* Create [Dev Test Result] page
* Update Jira Status 
* Log development time in Tempo under Epic card
* Follow Create PR Checklist below
Pull Request Creation Checklist
Draft Pull Request
* Create Draft PR first 
Proper title and description
* The title should have Jira Card so the PR will link back in the Jira  Development  section 
* Include brief description of the code changes to help reviewer understand the reason
* Also include  Related PRs  link(s) in the description if there are multiple PRs for the same feature/fix
* Include validation info: include screenshots or link to [Dev Test Result] page
Review your own changes carefully
* Make sure only your changes are in the PR you created
o If extra changes that are not your changes showed up in the PR, please talk to the code author who made those changes and find out why and explain that in the PR description
* Check if there are conflicts (don t resolve dev branch PR first if there is PR for release branch)
* Check for typos in method names, variable names etc.
* Check if unit tests, integration tests, Postman tests can be written
* Check for code styles and white space formatting (Reformat code at least match the surrounding code style and do manually code style fixes if necessary when the editor code formatter is not doing the necessary formatting) 
o Make sure to have some line spacing when needed (e.g. between two methods)
o Make sure NOT to have line spacing when NOT needed (e.g. no extra line spacing after return statement)
Ready for review
Click  Ready for review  button and assign reviewer(s) if needed
* Also see GitHub PRs: FAQs and Common Issues 
PR Reviewer Checklist
* Understand and check if code author follow Coding Checklists 
* Check to see if the code has unit/integration tests
* Check to have [Dev Test Result] page for Postman/API, UI and end-to-end tests
* Look at Jira and find related cards from Jira 
o Check Acceptance Criteria on the Jira 
o Check Jira requirements matches the code in the PR
Impact Analysis Checklist
* EFT Impact (sale transactions)
o VDI
o Mobile devices (Pico/Nano, 365pay etc.)
o V5/RT devices
o Stockwell
o Other integrations
* Database Impact
o DB Schema 365schema Guide 
* Application Performance
* Security (document existing security flaws if found and consider for security for technical implementation)
Note: Impact Analysis process can be skipped for simple change
Jira: User Story Checklist
* Understand the requirements: make sure that Jira has  Acceptance Criteria  in correct format and accounted for all scenarios including edge cases and error cases
o Developer should write the acceptance criteria for technical or production support related user stories and tasks
o For business use cases, ask product owner or Jira/ticket creator (PM, Epic owner etc.) to provide acceptance criteria and check if the provided acceptance criteria make sense.
````

## 78. Retail Standard-365Retail/Design/Solution+Document+Template.txt #0

Score: 1.000

````text
Solution Document Template
* 1 Document History
* 2 Purpose 
o 2.1 General Scope
o 2.2 Description
* 3 Open Questions
* 4. Project Success
* 5. Risk Level
* 6. Dependencies 
o 6.1 ADM
o 6.2 365pay/365Ops/Revolve App/Connect & Pay App
o 6.3 Pico/Mobile
o 6.4 V5/MM6/MM6 Mini
o 6.5 RT/MM6/MM6 Mini/CK for Dining
o 6.6 Avanti
o 6.7 Parlevel
o 6.8 Fullcount
o 6.9 Database
o 6.10 SOSLoad
o 6.11 Dashweb
o 6.12 API
o 6.13 Email API
o 6.14 AWS services
* 7 Design flow diagrams 
o 7.1 ADM > Section > Sub-section
o 7.2 UI/UX Flow diagram sub-section
o 7.3 Sequence Diagrams
* Compliance 
o PCI Impacts
o Personal Information Impacts
* 9 Data Sources
* 9 Database Requirements
* 10 Mobile App requirements
* 11 DevOps requirements
* 12 Special Notes
````

## 79. Retail Standard-365Retail/Design/Solution+Document+Template.txt #1

Score: 1.000

````text
VersionDatePrepared/Revised ByDescriptionMM/DD/YYYY Initial Draft            2 Purpose
2.1 General Scope
This will be the MVP product features on a high level.

2.2 Description
This text will outline the general flow of the MVP for delivery. Plus any issues that would limit or hinder development or deployment of the new feature or service.

3 Open Questions

QuestionAnswerResolution            
4. Project Success
This will be text which describes the key measurements of success for the project. Can be text accompanied by images.
This is where the level of risk is detailed.
Please break down risks by major systems and configurations that could be adversely effected.
6. Dependencies
6.1 ADM
This will be details of ADM dependencies and effects if applicable. Can be text accompanied by images.
6.2 365pay/365Ops/Revolve App/Connect & Pay App
This will be details of 365pay/365Ops/Revolve App/Connect & Pay App dependencies and effects if applicable. Can be text accompanied by images. Separate out into separate sections as needed.
6.3 Pico/Mobile
This will be details of Pico/Mobile impacts and effects if applicable. Can be text accompanied by images.
6.4 V5/MM6/MM6 Mini
This will be details of V5 impacts and effects if applicable. Can be text accompanied by images.
6.5 RT/MM6/MM6 Mini/CK for Dining
This will be details of RT impacts and effects if applicable. Can be text accompanied by images.
6.6 Avanti
This will be details of Avanti impacts and effects if applicable. Can be text accompanied by images.
6.7 Parlevel
This will be details of Avanti impacts and effects if applicable. Can be text accompanied by images.
6.8 Fullcount
This will be details of Avanti impacts and effects if applicable. Can be text accompanied by images.
6.9 Database
This will be details of Database dependencies and effects if applicable. Can be text accompanied by images.
6.10 SOSLoad
This will be details of SOSLoad impacts and effects if applicable. Can be text accompanied by images.
6.11 Dashweb
This will be details of Dashweb impacts and effects if applicable. Can be text accompanied by images.
6.12 API
This will be details of API impacts and effects if applicable. Can be text accompanied by images.
6.13 Email API
This will be details of Email API dependencies and effects if applicable. Can be text accompanied by images.
6.14 AWS services
This will be details of AWS service dependencies and effects if applicable. Can be text accompanied by images.

7 Design flow diagrams
7.1 ADM > Section > Sub-section
This can be written details and mocked-up interface changes.
7.2 UI/UX Flow diagram sub-section
This is how a sub-section should be displayed. This can include text and images as needed.
7.3 Sequence Diagrams
This is the flow of data documented. This can include text and images as needed.
Compliance
PCI Impacts
Personal Information Impacts
9 Data Sources
Table NameTable TypeLinked toLinked ColumnRemarks
9 Database Requirements
Field NameDescriptionDirect/
ComputedSource TableSource ColumnData TypeCalculation LogicDisplay Format10 Mobile App requirements
Include all necessary updates to 365pay/365Ops/Revolve App/Connect & Pay App including updated screens.
11 DevOps requirements
Include all necessary updates to environments.
12 Special Notes
This section is for special callouts and is optional based on need.
````

## 80. Retail Standard-365Retail/meeting-notes-in-space.md #0

Score: 1.000

````text
> Source: [https://nousteamdevx.atlassian.net/wiki/spaces/~712020a23ce38fee454c2db69cc12560ed1009/pages/589826](https://nousteamdevx.atlassian.net/wiki/spaces/~712020a23ce38fee454c2db69cc12560ed1009/pages/589826)
Create meeting note
````

## 81. Retail Standard-365Retail/meeting-notes-in-space.md #1

Score: 1.000

````text
Looking good, no incomplete tasks.
````

## 82. Retail Standard-365Retail/meeting-notes-in-space.md #2

Score: 1.000

````text
| Title | Decisions |
| --- | --- |
| No decisions found | |
````

## 83. Retail Standard-365Retail/meeting-notes-in-space.md #3

Score: 1.000

````text
| Title | Creator | Modified | |
| --- | --- | --- | --- |
| [2026-07-01 Meeting notes](/wiki/spaces/~712020a23ce38fee454c2db69cc12560ed1009/pages/393218/2026-07-01+Meeting+notes) | [Anurag Singh](/people/712020:a23ce38f-ee45-4c2d-b69c-c12560ed1009?ref=confluence) | Jul 01, 2026 | |
````
