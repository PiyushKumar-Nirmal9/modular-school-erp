# Project Statement: Modular School ERP

## 1. Problem Statement
Educational institutions often face administrative bottlenecks when coordinating student records, faculty management, library book circulation, transit operations, and fee assessment. Disconnected record-keeping systems cause synchronization issues (such as outdated bus route rosters when students enroll or unregistered borrowers checking out books). This project delivers a lightweight, unified Command-Line ERP system that persists and coordinates records across multiple modules without external database dependencies.

## 2. Scope of the Project
- **In Scope:**
  - Automated Student Information System (SIS) with dynamic grade and percentage calculations.
  - Faculty records directory with multi-field search and incremental salary updates.
  - Inventory-backed library check-out and return system with cross-role borrower verification.
  - Bus fleet and route management with auto-generated synchronized passenger manifests.
  - Performance-driven 5-tier fee categorization and scholarship qualification.
  - Class-level analytics including rank distributions, topper identification, and teacher mappings.
  - Persistent text-file data storage.
- **Out of Scope:**
  - Graphical User Interface (GUI) or web front-end.
  - Multi-user network concurrency or distributed database clustering.

## 3. Target Users
- **School Administrators:** Overseeing student registration, fee slab allocations, and bus route assignments.
- **Faculty & Academic Staff:** Managing exam marks, reviewing class rankings, and subject toppers.
- **Librarians:** Monitoring book stock, issuing assets to verified students and teachers, and logging returns.
- **Transport Coordinators:** Managing routes, drivers, and passenger logs.

## 4. High-Level Features
- **Centralized CLI Orchestrator:** Unified menu routing across 6 sub-systems.
- **Cross-Module Verification:** Real-time validation preventing orphaned records (e.g., student and teacher ID checks before book issuance).
- **Roster File Auto-Synchronization:** Automatic generation and updating of `route_<num>_details.txt` whenever student transit preferences change.
- **Persistent Flat-File Storage:** Pipe-delimited (`|`) file parsing ensuring session persistence without external libraries.
