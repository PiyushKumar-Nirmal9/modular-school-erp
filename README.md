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

-**Follow these sequential test scenarios to verify the application:**

-**Transport Setup:** Go to 4. Transport then‬ 1. Add Route. Enter Route 1, a bus number, and driver details. Verify that transport_routes.txt and route_1_details.txt are created.

-**Student Admission:** Go to 1. Student ‭then 1. Add New Student. Enter Class 10, Section A, and ID 101 (it auto-formats to S101). Choose School Transport Route 1 and enter marks. Verify that student_10_A.txt is updated and route_1_details.txt displays the student.

-**Validation & Duplicate Prevention:** Try re-adding a student with ID S101. Verify the system blocks it with an error message.

-**Faculty & Salary:** Go to 2. Teacher then1. Add Faculty. Enter details with ID 501 (formats to T501). Test the salary hike via Option 4 and verify the updated salary in teachers.txt.
-**Library Issue/Return:** Go to 3. Library then1. Add Book. Attempt to issue it to an invalid ID (e.g., S999) to confirm validation fails, then issue it to S101 to confirm stock decrements. Return the book to confirm stock restores.

-**Analytics & Fees:** Check 5. Student Fees to confirm the fee category and scholarship status for S101. Use 6. Class Module to view subject toppers and overall ranks.
