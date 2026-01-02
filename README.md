# Todo-application-by-Claude

A Spec-Driven Development (SDD) Todo Application built with Claude Code, featuring reusable intelligence agents, architectural governance, and test-driven workflows.

## Project Overview

This project demonstrates modern AI-assisted software development using Claude Code with Spec-Kit Plus methodology. It includes:

- **Constitution-based governance** - Clear architectural principles and decision-making framework
- **Intelligence agents** - Reusable subagents for spec creation, task management, planning, and implementation
- **Spec-driven workflow** - Full artifact generation (spec.md, plan.md, tasks.md) from feature descriptions
- **Console test runner** - Automated test execution and validation
- **Architectural Decision Records (ADRs)** - Documented significant decisions with rationale

## Features

- [x] Add Task - Create new todo items
- [ ] View Task List - Display all tasks
- [ ] Update Task - Modify existing tasks
- [ ] Delete Task - Remove completed items

## Project Structure

```
TodoApp/
├── .specify/              # SpecKit Plus templates and configuration
│   ├── memory/
│   │   └── constitution.md     # Project governance principles
│   └── templates/
├── specs/                 # Feature specifications and plans
│   ├── AddTask/
│   │   ├── spec.md              # User stories and acceptance criteria
│   │   ├── plan.md              # Architecture and API design
│   │   └── tasks.md             # Testable implementation tasks
├── src/                   # Implementation code
├── history/               # Prompt History Records (PHRs)
│   ├── prompts/                 # Full conversation transcripts
│   └── adr/                     # Architecture Decision Records
└── README.md              # This file
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher recommended)
- Git
- Claude Code CLI

### Installation

```bash
# Clone the repository
git clone https://github.com/majidali321/Todo-application-by-Claude.git
cd Todo-application-by-Claude

# Install dependencies (if package.json exists)
npm install
```

### Running Tests

```bash
# Run console test runner
npm test
# or
node tests/test-runner.js
```

### Using Claude Code

The project is designed to work with Claude Code CLI and its Spec-Kit Plus workflow:

```bash
# Create new spec from feature description
/sp.specify "User can view their task list sorted by due date"

# Generate implementation plan
/sp.plan

# Create actionable tasks
/sp.tasks

# Execute implementation
/sp.implement

# Document architectural decisions
/sp.adr "Authentication Strategy"
```

## Development Workflow

1. **Define Feature** - Describe user stories in natural language
2. **Generate Spec** - Run `/sp.specify` to create spec.md with acceptance criteria
3. **Create Plan** - Run `/sp.plan` to design architecture and APIs
4. **Define Tasks** - Run `/sp.tasks` to break down implementation
5. **Implement** - Run `/sp.implement` to execute tasks
6. **Document Decisions** - Use `/sp.adr` for significant architectural choices
7. **Commit & Push** - Track progress with git

## Architecture

### Core Principles

- **Explicit over implicit** - All behavior documented in specs
- **Smallest viable change** - Minimal, testable increments
- **Human as tool** - Clarify ambiguous requirements before proceeding
- **Architecture governance** - Constitution defines principles, ADRs document deviations

### Intelligence Agents

The project includes reusable agents for:
- **spec-writer** - Converts feature descriptions into formal specs
- **sqlmodel-schema-designer** - Designs database models
- **task-manager** - Implements Todo CRUD operations
- **frontend-component-builder** - Generates Next.js components
- **code-reviewer** - Validates quality and spec compliance

## Contributing

Contributions should follow the Spec-Driven Development methodology:

1. Create a feature spec in `specs/<feature-name>/spec.md`
2. Generate plan and tasks using Claude Code agents
3. Implement with test coverage
4. Document architectural decisions with ADRs
5. Create PHRs for all significant interactions

## Hackathon Reference

This project was developed for the AI Hackathon demonstrating:
- AI-assisted full-stack development
- Spec-driven architecture
- Reusable agent workflows
- Automated governance and documentation

## License

MIT License - See LICENSE file for details

## Contact

Built with [Claude Code](https://claude.com/claude-code) using Spec-Kit Plus methodology.

---

**Note**: This is Phase I of the Todo Application, focusing on the AddTask feature. Additional features (View, Update, Delete) will be added following the same spec-driven workflow.
