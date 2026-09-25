"""
class_analytics.py
Module 6: Section-level reports, toppers, rankings, and teacher mappings.
"""

import os
from config import TEACHER_FILE
from utils import get_student_file

def get_section_students(c_name, s_name):
    fname = get_student_file(c_name, s_name)
    if not os.path.exists(fname):
        return None

    students = []
    students2 = []
    with open(fname, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                students.append({
                    "id": parts[0],
                    "name": parts[1],
                    "dob": parts[2],
                    "class": parts[3],
                    "section": parts[4],
                    "subjects": parts[9],
                    "avg": float(parts[10]) if parts[10] != "N/A" else None,
                    "pct": float(parts[11]) if parts[11] != "N/A" else None,
                    "grade": parts[12]
                })
                students2.append({
                    "id": parts[0],
                    "name": parts[1],
                })
    return students2

def display_section_students_names():
    c_name = input("\nEnter Class (e.g. 10): ").strip()
    s_name = input("Enter Section (e.g. A): ").strip().upper()
    students = get_section_students(c_name, s_name)

    if students is None:
        print(f"Error: Record file for Class {c_name}-{s_name} does not exist.")
        return
    if not students:
        print(f"No student records found in Class {c_name}-{s_name}.")
        return

    print("\n" + "=" * 45)
    print(f"STUDENT LIST - CLASS {c_name}-{s_name}")
    print("=" * 45)
    print(f"{'SID':<15}{'Student Name'}")
    print("-" * 45)
    for s in students:
        print(f"{s['id']:<15}{s['name']}")
    print("=" * 45)

def display_section_subject_toppers():
    c_name = input("\nEnter Class (e.g. 10): ").strip()
    s_name = input("Enter Section (e.g. A): ").strip().upper()
    students = get_section_students(c_name, s_name)

    if students is None:
        print(f"Error: Record file for Class {c_name}-{s_name} does not exist.")
        return
    if not students:
        print(f"No student records found in Class {c_name}-{s_name}.")
        return

    subject_toppers = {}
    for s in students:
        if not s["subjects"] or s["subjects"] == "N/A":
            continue
        entries = s["subjects"].split(",")
        for item in entries:
            if ":" in item:
                sub, marks_str = item.split(":")
                marks = float(marks_str)
                if sub not in subject_toppers:
                    subject_toppers[sub] = {"top_mark": marks, "toppers": [(s["name"], s["id"])]}
                elif marks > subject_toppers[sub]["top_mark"]:
                    subject_toppers[sub] = {"top_mark": marks, "toppers": [(s["name"], s["id"])]}
                elif marks == subject_toppers[sub]["top_mark"]:
                    subject_toppers[sub]["toppers"].append((s["name"], s["id"]))

    if not subject_toppers:
        print("No subject marks have been recorded for this section yet.")
        return

    print("\n" + "=" * 65)
    print(f"HIGHEST SCORER PER SUBJECT - CLASS {c_name}-{s_name}")
    print("=" * 65)
    print(f"{'Subject':<18}{'Highest Mark':<15}{'Top Scorer(s)'}")
    print("-" * 65)
    for sub, data in sorted(subject_toppers.items()):
        toppers = ", ".join([f"{name} ({sid})" for name, sid in data["toppers"]])
        print(f"{sub:<18}{data['top_mark']:<15}{toppers}")
    print("=" * 65)

def display_section_ranks():
    c_name = input("\nEnter Class (e.g. 10): ").strip()
    s_name = input("Enter Section (e.g. A): ").strip().upper()
    students = get_section_students(c_name, s_name)

    if students is None:
        print(f"Error: Record file for Class {c_name}-{s_name} does not exist.")
        return
    if not students:
        print(f"No student records found in Class {c_name}-{s_name}.")
        return

    evaluated = [s for s in students if s["pct"] is not None]
    if not evaluated:
        print("No students in this section have marks recorded yet.")
        return

    ranked = sorted(evaluated, key=lambda s: s["pct"], reverse=True)
    max_pct = ranked[0]["pct"]
    min_pct = ranked[-1]["pct"]

    rank_1 = [s for s in ranked if s["pct"] == max_pct]
    last_rank = [s for s in ranked if s["pct"] == min_pct]

    print("\n" + "=" * 65)
    print(f"RANK 1 & LAST RANK - CLASS {c_name}-{s_name}")
    print("=" * 65)
    print("★ OVERALL RANK 1:")
    for s in rank_1:
        print(f"  - {s['name']} ({s['id']}) | Percentage: {s['pct']}% | Grade: {s['grade']}")

    print("\n▼ LAST RANK:")
    for s in last_rank:
        print(f"  - {s['name']} ({s['id']}) | Percentage: {s['pct']}% | Grade: {s['grade']}")
    print("=" * 65)

def display_section_scholarships():
    c_name = input("\nEnter Class (e.g. 10): ").strip()
    s_name = input("Enter Section (e.g. A): ").strip().upper()
    students = get_section_students(c_name, s_name)

    if students is None:
        print(f"Error: Record file for Class {c_name}-{s_name} does not exist.")
        return
    if not students:
        print(f"No student records found in Class {c_name}-{s_name}.")
        return

    scholars = [s for s in students if s["pct"] is not None and s["pct"] >= 96.0]

    print("\n" + "=" * 65)
    print(f"SCHOLARSHIP STUDENTS (>= 96%) - CLASS {c_name}-{s_name}")
    print("=" * 65)
    if not scholars:
        print("No students qualify for a scholarship in this section.")
    else:
        print(f"{'SID':<15}{'Student Name':<25}{'Percentage':<12}{'Grade'}")
        print("-" * 65)
        for s in scholars:
            print(f"{s['id']:<15}{s['name']:<25}{s['pct']:<12}{s['grade']}")
    print("=" * 65)

def display_class_teachers():
    """Displays all teachers teaching a specific class and section."""
    print("\n--- Teachers Assigned to Class ---")
    c_name = input("Enter Class (e.g. 10): ").strip()
    s_name = input("Enter Section (e.g. A): ").strip().upper()
    target_class = f"{c_name}-{s_name}"

    if not os.path.exists(TEACHER_FILE):
        print("No teacher records available.")
        return

    assigned = []
    with open(TEACHER_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                classes_taught = [cls.strip().upper() for cls in parts[4].split(",")]
                if target_class in classes_taught:
                    assigned.append(parts)

    print("\n" + "=" * 70)
    print(f"FACULTY LIST FOR CLASS {target_class}")
    print("=" * 70)
    if not assigned:
        print(f"No teachers are currently assigned to Class {target_class}.")
    else:
        print(f"{'FID':<10}{'Teacher Name':<22}{'Subject':<18}{'Email'}")
        print("-" * 70)
        for t in assigned:
            sub = t[5] if len(t) > 5 else "N/A"
            print(f"{t[0]:<10}{t[1]:<22}{sub:<18}{t[3]}")
    print("=" * 70)

def class_menu():
    while True:
        print("\n--- CLASS ANALYTICS MODULE ---")
        print("1. Display Students (Name and SID only)")
        print("2. Highest Scorer of Each Subject")
        print("3. Overall Rank 1 and Last Rank")
        print("4. Scholarship Students")
        print("5. View Teachers Teaching a Specific Class")
        print("6. Return to Main Menu")
        ch = input("Choose (1-6): ").strip()
        if ch == "1":
            display_section_students_names()
        elif ch == "2":
            display_section_subject_toppers()
        elif ch == "3":
            display_section_ranks()
        elif ch == "4":
            display_section_scholarships()
        elif ch == "5":
            display_class_teachers()
        elif ch == "6":
            break
        else:
            print("Invalid selection. Choose between 1 and 6.")
