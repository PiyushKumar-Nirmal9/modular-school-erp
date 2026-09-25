"""
teacher.py
Module 2: Teacher directory, search, and salary updates.
"""


import os
from config import TEACHER_FILE
from utils import format_teacher_id, teacher_exists

def print_teacher_card(parts):
    fid = parts[0]
    name = parts[1]
    contact = parts[2]
    email = parts[3]
    classes = parts[4]
    subject = parts[5] if len(parts) > 5 else "N/A"
    doj = parts[6] if len(parts) > 6 else "N/A"
    salary = parts[7] if len(parts) > 7 else "N/A"

    print(f"ID: {fid} | Name: {name} | Subject: {subject}")
    print(f"Contact: {contact} | Email: {email}")
    print(f"Date of Joining: {doj} | Salary: ${salary}")
    print(f"Classes Assigned: {classes}")
    print("-" * 80)

def add_teacher():
    print("\n--- Add Faculty Member ---")
    fid = format_teacher_id(input("Faculty ID (Unique): "))

    if teacher_exists(fid):
        print("Error: Faculty ID already registered.")
        return

    name = input("Teacher Name: ").strip()
    contact = input("Contact Details: ").strip()
    email = input("Teacher Email: ").strip()
    subject = input("Subject Taught: ").strip()
    doj = input("Date of Joining (DD-MM-YYYY): ").strip()

    while True:
        try:
            salary = float(input("Monthly Salary: ").strip())
            break
        except ValueError:
            print("Invalid salary amount. Please enter a valid number.")

    classes = input("Assigned Classes (e.g. 9-A, 10-B): ").strip()

    with open(TEACHER_FILE, "a") as f:
        f.write(f"{fid}|{name}|{contact}|{email}|{classes}|{subject}|{doj}|{salary:.2f}\n")
    print(f"Faculty member {name} added successfully with ID: {fid}.")

def display_teachers():
    print("\n--- Faculty List ---")
    if not os.path.exists(TEACHER_FILE):
        print("No teacher records found.")
        return

    with open(TEACHER_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("Teacher directory is empty.")
        return

    print("=" * 80)
    for line in lines:
        if line.strip():
            print_teacher_card(line.strip().split("|"))

def search_teacher():
    print("\n--- Search Faculty ---")
    if not os.path.exists(TEACHER_FILE):
        print("No teacher records found.")
        return

    print("Search by: [1] Faculty ID  [2] Faculty Name  [3] Subject")
    choice = input("Enter choice (1-3): ").strip()

    search_term = ""
    if choice == "1":
        search_term = format_teacher_id(input("Enter Faculty ID: "))
    elif choice == "2":
        search_term = input("Enter Faculty Name: ").strip().lower()
    elif choice == "3":
        search_term = input("Enter Subject: ").strip().lower()
    else:
        print("Invalid choice.")
        return

    matched_records = []
    with open(TEACHER_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                if choice == "1" and parts[0] == search_term:
                    matched_records.append(parts)
                elif choice == "2" and search_term in parts[1].lower():
                    matched_records.append(parts)
                elif choice == "3":
                    subj = parts[5].lower() if len(parts) > 5 else ""
                    if search_term in subj:
                        matched_records.append(parts)

    if matched_records:
        print(f"\n--- Search Results ({len(matched_records)} found) ---")
        print("=" * 80)
        for parts in matched_records:
            print_teacher_card(parts)
    else:
        print("No matching teacher record found.")

def increment_salary():
    print("\n--- Salary Increment ---")
    if not os.path.exists(TEACHER_FILE):
        print("Teacher directory does not exist.")
        return

    fid = format_teacher_id(input("Enter Faculty ID for salary increment: "))
    updated = False
    new_lines = []

    with open(TEACHER_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split("|")
        if parts[0] == fid:
            updated = True
            current_salary = float(parts[7]) if len(parts) > 7 else 0.0
            print(f"Teacher: {parts[1]} | Current Salary: ${current_salary:.2f}")
            print("Increment Type: [1] Percentage (%)  [2] Fixed Amount")
            inc_type = input("Choose (1/2): ").strip()

            if inc_type == "1":
                pct = float(input("Enter percentage increment (e.g., 10 for 10%): ").strip())
                new_salary = current_salary + (current_salary * pct / 100)
            elif inc_type == "2":
                amount = float(input("Enter fixed hike amount: ").strip())
                new_salary = current_salary + amount
            else:
                print("Invalid choice. Increment cancelled.")
                new_lines.append(line)
                continue

            while len(parts) < 8:
                parts.append("N/A")
            parts[7] = f"{new_salary:.2f}"
            new_lines.append("|".join(parts) + "\n")
            print(f"Salary updated to: ${new_salary:.2f}")
        else:
            new_lines.append(line)

    if updated:
        with open(TEACHER_FILE, "w") as f:
            f.writelines(new_lines)
    else:
        print("Faculty ID not found.")

def teacher_menu():
    while True:
        print("\n--- TEACHER CORNER ---")
        print("1. Add Faculty Record")
        print("2. Display All Teachers")
        print("3. Search Teacher (by ID, Name, or Subject)")
        print("4. Increment Teacher Salary")
        print("5. Return to Main Menu")
        ch = input("Choose (1-5): ").strip()
        if ch == "1":
            add_teacher()
        elif ch == "2":
            display_teachers()
        elif ch == "3":
            search_teacher()
        elif ch == "4":
            increment_salary()
        elif ch == "5":
            break
        else:
            print("Invalid option.")
