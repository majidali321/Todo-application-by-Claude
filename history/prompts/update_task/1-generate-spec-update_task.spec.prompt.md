---
id: 1
title: Generate spec for UpdateTask skill
stage: spec
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: update_task
branch: master
user: TBD
command: Generate spec for UpdateTask reusable skill
labels: [spec, update-task, task-manager]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/features/update_task.md
tests:
 - N/A
---

## Prompt

GENERATE SPEC FOR UPDATETASK SKILL

Task: Generate detailed Markdown spec for the fourth reusable skill: UpdateTask

File path: specs/features/update_task.md

Requirements:
- Method: update_task(self, task_id: int, title: str | None = None, description: str | None = None) -> dict
- Find task by ID
- Update only provided fields (title and/or description)
- Leave other fields unchanged
- Return updated task dict
- Raise ValueError if ID not found or no updates provided

Spec structure same as previous specs (Feature Name, Description, Requirements, Parameters table, Output, Examples, Edge Cases)

## Response snapshot

Created comprehensive specification file at specs/features/update_task.md following the same structure as previous skill specs (AddTask, ViewTaskList, MarkTaskComplete). The spec includes:

- Complete feature description and user stories (2 stories)
- 7 detailed functional requirements covering method signature, task lookup, partial update logic, validation, return value, in-memory modification, and clean code compliance
- Detailed parameters table with types, defaults, and descriptions
- Output format with JSON schema
- 8 code examples covering all update scenarios (title only, description only, both fields, clear description, error handling)
- Comprehensive edge cases table with 12 scenarios
- References to constitution principles (Reusable Intelligence, Clean Code, Defensive Programming, Testability)
- 15 acceptance criteria covering all functional aspects and edge cases
- Non-functional requirements for performance, maintainability, data integrity, and scalability
- Implementation notes with class structure, key details, validation order, and transactional update approach
- Related features section and change history table

## Outcome

- ✅ Impact: Created complete, production-ready specification for UpdateTask skill
- 🧪 Tests: N/A
- 📁 Files: Created specs/features/update_task.md (314 lines) with comprehensive specification
- 🔁 Next prompts: Implement update_task method and add menu option in console runner
- 🧠 Reflection: Successfully followed existing spec structure and conventions; included all required sections plus additional detail for partial update behavior

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
