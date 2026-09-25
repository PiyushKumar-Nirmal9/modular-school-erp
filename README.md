# Modular School ERP (CLI)

## Overview
A lightweight, terminal-based enterprise management system written in modular Python. It centralizes institutional record-keeping across academic, administrative, and logistical domains using persistent flat-file data storage.

### Key Functional Modules
1. **Student & Grade Operations:** Profile lifecycle (CRUD), automated GPA/grade calculation, and subject performance tracking.
2. **Faculty Administration:** Faculty registry, multi-parameter directory search, and automated salary revision tools.
3. **Library Management:** Catalog index, copy availability management, and dual-entity borrow/return workflows.
4. **Transport Logistics:** Route creation, roster compilation, and synchronized student commute management.
5. **Fee & Scholarship Profiling:** Merit-driven slab categorization and fee discount eligibility computation.
6. **Class Analytics:** Subject topper extraction, section rankings, and teacher-class mapping.

### Non-Functional Requirements
- **Modularity:** Structured across 8 decoupled script modules with explicit separation of concerns.
- **Portability & Zero Dependencies:** Operates entirely on Python 3 standard libraries with no third-party package dependencies.
- **Data Persistence:** Text-based flat-file storage ensuring state retention across user sessions.
- **Input Robustness & Validation:** Type checking, strict ID formatting (e.g., `S` prefix for students, `T` for teachers), and graceful error recovery.
