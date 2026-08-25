# Golden Repository Implementation Guidelines

Generated for: InternTest
Repository: DEVXADO,Retail Standard-365Retail
Generated at: 2026-08-25T09:38:39.265Z
File selection mode: all vectorized files

## Warnings

- None

## How To Use

- Read this file before implementation in the IDE.
- Use `golden-repo-sources.md` for exact source excerpts and file-path attribution.
- Use Golden Repo guidance for conventions, patterns, validation expectations, architecture style, testing expectations, and implementation constraints.
- Do not invent product scope, endpoints, screens, fields, permissions, jobs, or workflows from Golden Repo guidance alone.
- Existing code patterns in the target workspace override generic Golden Repo guidance when they conflict.
- Do not require live Golden Repository access inside the implementation workspace.

## Extracted Guidance

GOLDEN REPO KNOWLEDGE CONTEXT (spec generation)
Repository: DEVXADO,Retail Standard-365Retail
The following is a distilled, de-duplicated consolidation of the Golden Repository standards and reference guidance (summarized from the full corpus to preserve all distinct constraints without repetition). Use it as guidance only. It may define terminology, architecture conventions, validation expectations, examples, and output style. Do not extract or invent product scope, endpoints, screens, fields, or requirements from this guidance alone.

## Architecture & System Design

### Platform Scope and Organizational Boundary

- Implement the solution within Azure DevOps.
- Operate within the **My Team** organization boundary; all projects, documentation, and tasks are scoped to that organization.

### Portfolio Structure and Work Hierarchy

- Organize scope under one epic with these three features:
  - **Project Lifecycle Management**
  - **BRD Creation and Document Management**
  - **Task Management and Team Collaboration**
- Significant changes are tracked as **Epics**.

### Access, Roles, and Supported Users

- Support role-based access control at the project level.
- Support all registered team members.

### Business Rules and Enforcement

- Enforce business rules at the system level, not only the UI.
- Ensure business rule enforcement is consistent across UI and API with **100% consistency**.

### Capacity and Scale Requirements

- Support at least **50 active concurrent projects** without degradation.
- Support at least **200 tasks per project**.
- Retain **unlimited BRD version history**.

### Required Design and Solution Documentation

- Solution/project design documents should include:
  - Document History
  - Purpose
  - Open Questions
  - Project Success
  - Risk Level
  - Dependencies
  - Design flow diagrams
  - Compliance
  - Data Sources
  - Database Requirements
  - Mobile App requirements
  - DevOps requirements
  - Special Notes

### Compliance, Governance, Security, and Privacy by Design

- Add a **Compliance & Governance** section in project charters / solution designs covering:
  - Subject to **365 Information Security Policy and SDLC**
  - Whether the change requires **DPIA update under SOS 47951**
  - **PCI/PII** handling, including encryption and transmission requirements
- Security and privacy controls must be embedded across:
  - requirements
  - design
  - implementation
  - verification
  - release
  - response

### Documentation Traceability for Security and Release

- Documentation for a project/feature should show:
  - where security/privacy requirements are defined
  - how they are tested/verified
  - how changes are approved and released

## API & Integration Conventions

### API Behavior and Validation

- API access must enforce the same business rules as the user interface.
- For task assignment, the system must display an error if a non-associated member is assigned via API.

### Integration Standards

- Use native Azure DevOps integration.
- Support the organization’s standard authentication mechanisms via organizational SSO/identity provider.

### Governance and Compliance for New Integrations

- For any new integration or process, ensure:
  - A clear owner is identified (Information Owner).
  - Auditability is provided with logs, reports, and documentation retained for at least 5 years.
  - Alignment with GDPR and US privacy governance requirements if end-user data is involved.

## Data Model & Validation

### Project Entity & Validation

- Project creation requires these mandatory fields:
  - `Project Name`
  - `Status`
  - `Owner`
- Prevent project submission when any mandatory field is empty.
- Set the default project status to `Not Started` on creation.
- Generate a unique project identifier on successful creation.
- Each project must have a designated owner at creation; orphaned projects are not permitted.
- Owner selection must be restricted to registered team members.

### Project Status Model

- Project status flow must be:
  - `Not Started -> In Progress -> Completed`
- Block invalid project status transitions, including:
  - `Not Started -> Completed`
- Only present valid next project statuses based on the current state.
- Record the timestamp and user identity for every project status transition.

### Project Team Member Associations

- Only the project owner may add team members.
- Each associated team member must have a project-specific role.
- Duplicate team member associations are not permitted.
- Maintain a record of team member associations.
- Only associated team members may perform project-specific activities.

### BRD Data Model, Template, and Validation

- Each BRD must:
  - follow a fixed standardized organizational template
  - be associated with exactly one parent project
  - start at version `1.0`
  - start in status `Draft`
- BRD template sections must include:
  - Executive Summary
  - Purpose & Scope
  - Business Objectives
  - Functional Requirements
  - Non-Functional Requirements
- Auto-populate BRD document control fields:
  - creation date
  - version number
  - author

### BRD Versioning & Publishing Rules

- BRD draft saves must not increment the version number.
- Increment the BRD version only when it is explicitly published.
- Require a change summary before publishing a new BRD version.
- Maintain version history including:
  - published versions
  - date
  - change summary
- Previous BRD versions must remain accessible in read-only format.

### BRD Search & Retrieval

- Full-text BRD search must cover both titles and content.
- BRD search filters must support:
  - project
  - status (`Draft` / `Published`)
  - date range
- Search results must default to showing the most recent version of each BRD.

### Task Entity & Validation

- Task creation rules:
  - `Title` is mandatory
  - `Description`, `Priority`, `Due Date`, and `Assignee` are optional
  - each task must be associated with exactly one parent project
- Generate a unique task identifier on creation.
- Initial task status must be `To Do`.
- Restrict task assignee selection to team members currently associated with the project.

### Task Status Model

- Task status flow must be:
  - `To Do -> In Progress -> Done`
- Only present valid next task statuses based on the current state.
- Record the timestamp and user identity for every task status change.

### Derived Task State & Dashboard Constraints

- Overdue tasks are defined as tasks whose due date has passed and whose status is not `Done`.
- The personal dashboard must show all tasks assigned to the logged-in user across associated projects.
- Dashboard task lists must be organized or sortable by:
  - priority
  - due date

## Security & Compliance

### Access Control and Authorization

- Restrict access to project data to associated team members only.
- Restrict BRD search results to projects the user is associated with; enforce this restriction at the query level.
- Restrict task status updates to authorized users only:
  - the assignee, or
  - the project owner.
- All user actions must be attributable to an authenticated identity.

### Data Protection and Classification

- Protect all information against unauthorized modification, destruction, or disclosure throughout its lifecycle.
- Classify data by sensitivity, for example:
  - PHI
  - PII
  - PCI
  - CI
  - Internal
- Apply the same data classification consistently across all formats, including:
  - source
  - database
  - report
  - export

### Secure Transmission and Sharing

- Sensitive data transmission must use secure protocols such as:
  - TLS
  - SSL
  - IPsec
  - SFTP
- Do not send sensitive data via unencrypted:
  - email
  - SMS
  - IM
- Use secure external file sharing for sensitive data, such as:
  - encrypted links
  - password-protected files

### Privacy by Design and Compliance Review

- Implement Data Protection by Design and Privacy by Default in the product development lifecycle.
- New or changed features on in-scope products may require DPIA review or updates if they change:
  - data flows
  - data types
  - risk
- Product and feature specifications should explicitly call out:
  - data collected, stored, and transmitted, and its classification
  - where encryption at rest and in transit applies
  - the retention model
  - the access control model
- The Compliance section in solution documentation must cover:
  - PCI impacts
  - Personal Information impacts

### Governance, Policies, and Regulatory Compliance

- Policies and procedures must be:
  - documented
  - available to responsible individuals
  - retained for at least 5 years
  - periodically reviewed and updated
- Information Security Team responsibilities include:
  - conducting audits
  - ensuring compliance with applicable laws, including:
    - GDPR
    - CCPA
    - CPRA
    - FCRA
    - HIPAA
    - BIPA
    - GLBA

### Immutable Published Records

- Published BRD versions cannot be modified or deleted after publication.

### Secure Logging Practices

- In Java logging:
  - use parameterized SLF4J messages
  - do not log credentials; mask credentials if output is necessary
  - avoid unnecessary logging such as object lists or development debugging output at info level

## Testing & Quality Expectations

### Required Test Coverage

- Test and verify all changes.
- Write unit tests and integration tests.
- For Java/Kotlin projects, use `./gradlew build`.
- Run static analysis and linting as applicable:
  - Run SpotBugs for Java/Kotlin.
  - Run ESLint for JavaScript/TypeScript.

### PR and Code Review Quality Gates

- PRs and reviews should check whether unit tests, integration tests, and Postman tests can be written.
- PR reviewers should verify that code includes unit and integration tests.
- PR reviewers should verify that a Dev Test Result page exists covering:
  - Postman/API tests
  - UI tests
  - End-to-end tests
- Review the commit diff to:
  - Remove extra changes
  - Fix typos
  - Improve comments
- Reformat code to match the surrounding code style.

### Dev Test Result Documentation

- Create a `[Dev Test Result]` page.
- Ensure the Dev Test Result page documents results for:
  - Postman/API tests
  - UI tests
  - End-to-end tests

### Acceptance Criteria and Scenario Coverage

- Acceptance criteria in Jira must account for all scenarios, including:
  - Edge cases
  - Error cases
- For technical or production-support user stories/tasks, developers should write the acceptance criteria.
- For business use cases:
  - Obtain acceptance criteria from the product owner or ticket creator.
  - Validate that the acceptance criteria make sense.

### Security, Privacy, and Compliance Validation

- Integrate audit, penetration testing, and vulnerability remediation into the delivery lifecycle.
- Show how security and privacy requirements are tested and verified, including:
  - Functional tests
  - Penetration tests
  - Privacy tests

## UI/UX & Accessibility

### Forms and Data Entry

- Clearly mark mandatory fields on all forms with visual indicators.
  - Project creation forms must clearly mark mandatory fields.
- Validation errors must clearly identify missing required data with specific field-level messaging.
- BRD creation forms must display standardized template sections.

### Context-Sensitive UI Behavior

- Present only valid next-status options to users via context-sensitive UI controls.

### Dashboard UX

- Visually highlight overdue tasks on personal dashboards with distinct visual treatment.
- Provide direct navigation from the dashboard to:
  - Task details
  - Parent project context

## Domain & Business Rules

### Project Ownership and Accountability

- Every project must have a designated owner.
- Project creation must support structured initialization with mandatory ownership.
- The project owner is accountable for:
  - project delivery
  - team composition
- All activities must be traceable to responsible individuals.
- Maintain an auditable history of:
  - project decisions
  - changes
  - actions

### Team Membership and Participation Rules

- User provisioning must occur before a user can participate in a project.
- Only registered team members may participate in project activities.
- Team composition management is restricted to the owner role.
- Only team members associated with the parent project may perform project activities within that project, including:
  - task assignment
  - BRD editing
- Only team members associated with the parent project may edit BRDs within that project.

### Tasks and Project Progress Rules

- Tasks provide granular work breakdown within the context of a project.
- Task status changes must automatically recalculate the completed task percentage at the project level.
- A personal dashboard must provide a consolidated view of tasks assigned to an individual across all projects.

### BRD Lifecycle Rules

- BRD lifecycle statuses are:
  - `Draft`
  - `Published`
- A `Published` BRD version is formally released and immutable.

### Documentation and Audit Standards

- Documentation must follow organizational standards.

## Naming, Structure & Code Patterns

### Pull Requests & Commits

- Use meaningful commit messages in the required format.
- Create a Draft PR first.
- Include the Jira card in the PR title so the PR links back in the Jira Development section.
- Ensure the PR description includes:
  - a brief description of the code changes
  - links to related PRs if multiple PRs exist for the same feature or fix
  - validation information, such as screenshots or a Dev Test Result link
- Review your own PR before requesting review to ensure only intended changes are included.

### Naming & API Design

- Check for typos in method names and variable names.
- Avoid boolean parameters in methods.

### Access Control & Documentation

- Minimize the accessibility of classes and members.
- Use JavaDoc when necessary.

### Code Style & Formatting

- Maintain code style and whitespace formatting.
- Manually fix formatting if the editor formatter is insufficient.
- Include line spacing between methods when needed.
- Do not add unnecessary line spacing, such as after a `return` statement.

## Error Handling & Resilience

### Validation Errors

- Display a validation error when saving a project without all mandatory fields.
- Display an error if a non-associated member is assigned to a task via API.

### Authorization and Association Errors

- Block task status updates from unauthorized team members and display an appropriate error message.
- Block duplicate team member associations and display an error if the member is already associated.

### State Transition and Immutability Protections

- Block invalid project status transitions and display an error or notification.
- Ensure version history is immutable once published.

### Data Resilience and Integrity

- Persist all saved data without loss, with 99.9% data integrity.

## Performance & Observability

### Performance Targets

- BRD search results must return within `<= 2 seconds`.
  - Include relevant context snippets in BRD search results.
- Project creation form must load within `<= 3 seconds`.
- Page load times for all system views must remain `<= 3 seconds` under normal load.
- Task status updates must be reflected immediately upon save; target real-time.
- Dashboard data must refresh in near-real-time within `<= 5 seconds`.
- Dashboard and task status views require real-time or near-real-time refresh.

### Performance Review and Analysis

- Check database query performance.
- Impact analysis should consider:
  - EFT impact
  - database impact
  - application performance
  - security
- Impact analysis process can be skipped for simple changes.

### Observability and Audit Logging

- Log status transitions and association changes for audit purposes.

### Audit and Compliance Reviews

- Systems processing PHI/PII/PCI/CI/internal info are subject to yearly systems audits.
- Non-compliant audit items must be documented, tracked, and remediated via change management.
- Policy itself is reviewed yearly; changes tracked in document revisions.