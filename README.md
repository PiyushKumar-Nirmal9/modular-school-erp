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

## Technologies Used
- **Language:** Python 3 (standard library only)
- **Data Persistence:** Plain-text flat files with pipe-delimited records (`.txt`)
- **Version Control:** Git & GitHub

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/PiyushKumar-Nirmal9/modular-school-erp.git](https://github.com/PiyushKumar-Nirmal9/modular-school-erp.git)
   cd modular-school-erp
2. python3 --version
3.  python3 main.py 
---

### 4. Check for Missing Code Files in the Repository

Looking at your files list[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span):
* You have `main.py`, `utils.py`, `config.py`, `student.py`, `teacher.py`, `library.py`, `transport.py`, `fee.py`, and `class_analytics.py`[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span).
* Check that **all** `.py` files inside the repository were uploaded with the `sys.path.insert(...)` fix so the evaluator encounters no import issues when running `python3 main.py`[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span).

---

### 5. Required Next Step: Project Report Submission (PDF)

The GitHub repository accounts for **10%** of your grade[span_22](start_span)[span_22](end_span). According to **Section 6 & 7 (Evaluation Rubric)**, you still need to complete the **Project Report PDF (20%)** and submit it to the portal[span_23](start_span)[span_23](end_span). 

Ensure your report includes the 15 required sections (System Architecture, Use Case / Sequence / Workflow Diagrams, and Screenshots)[span_24](start_span)[span_24](end_span).

