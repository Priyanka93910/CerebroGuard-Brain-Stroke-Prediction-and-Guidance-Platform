# Golden Repository UI/UX Design System

Generated for: InternTest
Repository: DEVXADO,Retail Standard-365Retail
Generated at: 2026-08-25T09:38:39.272Z

## Warnings

- None

## How To Use

- Read this file before UI implementation to align with the Golden Repository design language.
- Apply these design tokens, component rules, and accessibility requirements when building UI.
- Use `golden-ui-design-sources.md` for the exact UI/design source excerpts and file-path attribution.
- Existing UI conventions in the target workspace override generic guidance when they conflict.
- Do not invent tokens, components, screens, or flows that are not defined here.
- Do not require live Golden Repository access inside the implementation workspace.

## Design System

## Design Principles & Brand

### Core Product Principles

- Enforce data completeness at creation time for required records.
- Mandatory ownership is required for projects; orphaned projects are not permitted.
- Standardized documentation formats are fixed by the organization and cannot be modified by individual users.
- Business rules must be enforced consistently across the UI and API.

### Privacy by Design Principles

- Privacy requirements must be reflected in requirements and design, including:
  - Data Protection by Design
  - Privacy by Default
  - data minimization
  - access controls
  - retention considerations

### Security & Privacy Lifecycle Integration

- Security and privacy controls must be embedded across all lifecycle stages:
  - Requirements
  - Design
  - Implementation
  - Verification
  - Release
  - Response

## Components & Patterns

### Project Creation

- Clearly mark mandatory fields.
- Required fields:
  - Project Name
  - Status
  - Owner
- Prevent submission when any mandatory field is empty.
- If save is attempted with incomplete mandatory fields, display a validation error.
- Owner selection uses a dropdown of registered team members.
- Exactly one owner must be selected before saving.
- Default Status on creation: `Not Started`.
- Generate a unique project identifier on successful creation.

### Project Status Transitions

- Only present valid next-status options based on the current state.
- Valid transitions:
  - `Not Started → In Progress`
  - `In Progress → Completed`
- Block invalid transitions.
- On invalid transition attempt, display an error message or notification.
- Record timestamp and user identity for each transition.

### BRD Creation

- BRD creation form is shown within a project context.
- Use a standardized template structure.
- Include these sections:
  - Executive Summary
  - Purpose & Scope
  - Business Objectives
  - Functional Requirements
  - Non-Functional Requirements
- Auto-populate document control fields:
  - project name
  - creation date
  - version number
  - author
- Associate each BRD with exactly one parent project.
- Initial BRD version: `1.0`.
- Initial BRD status: `Draft`.

### Task Creation

- Task creation form is shown within project context.
- Mandatory field:
  - Title
- Optional fields:
  - Description
  - Priority
  - Due Date
  - Assignee
- Associate each task with exactly one parent project.
- Generate a unique task identifier on creation.
- Initial task status: `To Do`.

### Task Assignment Rules

- Assignee selection is restricted to team members associated with the project.
- If a non-associated member is assigned via API, show an error.

### Task Status Updates

- Only the task assignee or project owner may update task status.
- Other team members must be blocked and shown an appropriate error message.
- Only display valid next statuses based on the current state.
- Valid task progression:
  - `To Do → In Progress → Done`
- Reflect updates immediately upon save across relevant views.
- Record timestamp and user identity for each status change.
- Automatically recalculate project-level completed task percentage after task status changes.

### Personal Task Dashboard

- Display all tasks assigned to the logged-in user across all associated projects.
- Organize or allow sorting by:
  - project
  - status
- Provide direct navigation to:
  - task details
  - parent project context
- Tracking information must be accessible to relevant team members.

## Interaction & Motion

### Form and Input Validation

- Prevent form submission when required fields are empty.

### Real-Time and Update Behavior

- Reflect task status updates immediately upon save.
- Task status updates target: real-time.
- Dashboard data refresh target: near-real-time, `≤ 5 seconds`.

### Performance Targets

- General page load target under normal load: `≤ 3 seconds`.
- Project creation form load target: `≤ 3 seconds`.
- BRD search results target: `≤ 2 seconds`.

## Accessibility

### Form requirements and validation

- Clearly mark all mandatory fields on forms.
- Validation errors must clearly identify missing required data.
- Use specific, field-level validation messaging.

### Context-sensitive controls

- Present only valid next-status options to users via context-sensitive UI controls.

## Iconography & Imagery

### Status-Based Visual Treatment

- Overdue tasks on the personal dashboard must be visually highlighted with a distinct visual treatment.
- A task is overdue when:
  - its due date has passed, and
  - its status is not `Done`

### Documentation Imagery

- Solution and design documentation may include mocked-up interface changes, text, and images.
- Project success and dependency sections in solution documentation may be accompanied by images.

## UI Naming & Structure

### Status Naming

- Project statuses:
  - `Not Started`
  - `In Progress`
  - `Completed`

- Task statuses:
  - `To Do`
  - `Done`

- BRD status:
  - `Draft`

### Dashboard Structure

- Personal dashboard:
  - Consolidated view of all tasks assigned to an individual across projects.

### Document Information Architecture

- Solution document / design structure includes:
  - Document History
  - Purpose
  - General Scope
  - Description
  - Open Questions
  - Project Success
  - Risk Level
  - Dependencies
  - Design flow diagrams
  - ADM > Section > Sub-section
  - UI/UX Flow diagram sub-section
  - Sequence Diagrams
  - Compliance
  - PCI Impacts
  - Personal Information Impacts
  - Data Sources
  - Database Requirements
  - Mobile App requirements
  - DevOps requirements
  - Special Notes