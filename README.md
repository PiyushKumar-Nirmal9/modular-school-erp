# Modular School ERP (CLI)

## Overview
A lightweight, terminal-based enterprise management system written in modular Python. It centralizes institutional record-keeping across academic, administrative, and logistical domains using persistent flat-file data storage.

## Features
1. **Student & Grade Operations:** Profile lifecycle management (CRUD), automated GPA/grade calculation, and subject performance tracking.
2. **Faculty Administration:** Faculty registry, multi-parameter directory search (by ID, Name, or Subject), and salary revision tools.
3. **Library Management:** Catalog index, copy availability management, and dual-entity borrow/return workflows with ID verification.
4. **Transport Logistics:** Route creation, roster compilation, and synchronized student commute management.
5. **Fee & Scholarship Profiling:** Merit-driven slab categorization (Categories 1–5) and fee discount eligibility computation.
6. **Class Analytics:** Subject topper extraction, section rankings (Rank 1 and Last Rank), and teacher-class mapping.

## Non-Functional Requirements
- **Modularity:** Structured across decoupled script modules with explicit separation of concerns.
- **Portability & Zero Dependencies:** Operates entirely on Python 3 standard libraries with no third-party package dependencies.
- **Data Persistence:** Text-based flat-file storage ensuring state retention across user sessions.
- **Input Robustness & Validation:** Type checking, strict ID formatting (e.g., `S` prefix for students, `T` for teachers), and graceful error recovery.

## Technologies Used
- **Language:** Python 3 (standard library only)
- **Data Persistence:** Plain-text flat files with pipe-delimited records (`.txt`)
- **Version Control:** Git & GitHub

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/PiyushKumar-Nirmal9/modular-school-erp.git
cd modular-school-erp
```
2.Verify Python 3 is installed:
```bash
python3 --version
```
3.Run the application:
```bash
python3 main.py
```
## Instructions for Testing

1. **Student Module:** 
   - Select option `1` -> `1` to add a new student (e.g., SID `S101`, Class `10`, Section `A`).
   - Select option `1` -> `2` for Class `10` and Section `A` to view the student profile and calculated grades.
2. **Library Validation:**
   - Select option `3` -> `3` to issue a book. Test with an unregistered borrower ID to verify validation failure.
   - Enter a registered ID (`S101` or a registered Faculty ID) to verify issuance and inventory deduction.
3. **Transport Synchronization:**
   - Add a student with the `School Transportation` option enabled.
   - Select option `4` -> `3` to inspect the dedicated `route_<num>_details.txt` file and confirm the student appears on the passenger manifest.
4. **Class Analytics:**
   - Select option `6` -> `2` and `6` -> `3` for Class `10` Section `A` to test subject topper extractions and section ranking distribution.
