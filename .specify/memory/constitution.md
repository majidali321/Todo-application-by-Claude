<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: All principles and sections
Removed sections: N/A
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# TodoApp Constitution

## Core Principles

### SPEC-DRIVEN DEVELOPMENT
All features must be specified before implementation using the spec-driven workflow. Specifications must include user stories, acceptance criteria, and detailed requirements before any code is written.

### REUSABLE INTELLIGENCE
Code components must be designed as reusable, modular units with clear interfaces. Methods should follow clean code principles with type hints, comprehensive documentation, and defensive programming practices.

### CLEAN CODE STANDARDS
All code must follow clean code principles with proper type hints, comprehensive documentation (docstrings), and single responsibility. Methods must have clear input/output contracts and be independently testable.

### DEFENSIVE PROGRAMMING
Robust error handling and input validation must be implemented. Validate all inputs before modifying state, ensure proper error messages, and protect critical data integrity.

### TEST-FIRST APPROACH
Test-driven development is mandatory: write tests first, ensure they fail, then implement code to make them pass. Follow the Red-Green-Refactor cycle strictly.

### ARCHITECTURAL GOVERNANCE
All significant architectural decisions must be documented as Architecture Decision Records (ADRs). Follow the three-part test for ADR significance: impact, alternatives, scope.

## Security Requirements

Never hardcode secrets or tokens; use .env files and documentation. Follow security best practices for all user inputs and data handling.

## Development Workflow

Use the Spec-Driven Development workflow: /sp.specify → /sp.plan → /sp.tasks → /sp.implement. Create PHRs for all significant interactions and follow the human-as-tool strategy for clarifications.

## Governance

All implementations must comply with the principles in this constitution. Amendments require documentation and proper versioning. The constitution supersedes all other practices. All code must reference this constitution in specifications.

**Version**: 1.0.0 | **Ratified**: 2026-01-20 | **Last Amended**: 2026-01-20
