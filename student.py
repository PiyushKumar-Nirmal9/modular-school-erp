"""
student.py
Module 1: Student profiles, mark entry, and student CRUD operations.
"""
import os
from utils import (
    format_student_id,
    get_student_file,
    student_exists_anywhere,
    sync_route_files,
    select_transport_option
)

def calculate_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 50:
        return "D"
    else:
        return "F"

def add_student():
    print("\n--- Add Student Record ---")
    c_name = input("Enter Class (e.g. 10): ").strip()
    s_name = input("Enter Section (e.g. A): ").strip().upper()
    fname = get_student_file(c_name, s_name)

    raw_sid = input("Enter Unique Student ID: ").strip()
    sid = format_student_id(raw_sid)
    
    if student_exists_anywhere(sid):
        print(f"Error: Student ID '{sid}' already exists.")
        return

    name = input("Enter Student Name: ").strip()
    dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
    contact = input("Enter Student Contact Info: ").strip()
    p_name = input("Enter Parent Name: ").strip()
    p_contact = input("Enter Parent Contact: ").strip()
    p_job = input("Enter Parent Job Details: ").strip()
    parent_info = f"{p_name};{p_contact};{p_job}"
    email = input("Enter Student Email: ").strip()

    trans_mode = select_transport_option()

    print("\n-- Subject Marks Input --")
    enter_marks = input("Do you want to enter marks now? (y/n): ").strip().lower()
    
    if enter_marks == 'y':
        sub_count_input = input("How many subjects? ").strip()
        sub_count = int(sub_count_input) if sub_count_input.isdigit() else 0
    else:
        sub_count = 0

    if sub_count > 0:
        sub_records = []
        total_marks = 0.0
        for i in range(sub_count):
            sub = input(f"Enter name of subject {i+1}: ").strip()
            marks = float(input(f"Enter marks obtained in {sub} (out of 100): "))
            sub_records.append(f"{sub}:{marks}")
            total_marks += marks

        avg_marks = str(round(total_marks / sub_count, 2))
        percentage = avg_marks
        overall_grade = calculate_grade(float(percentage))
        sub_str = ",".join(sub_records)
    else:
        sub_str = "N/A"
        avg_marks = "N/A"
        percentage = "N/A"
        overall_grade = "N/A"

    record = f"{sid}|{name}|{dob}|{c_name}|{s_name}|{contact}|{parent_info}|{email}|{trans_mode}|{sub_str}|{avg_marks}|{percentage}|{overall_grade}\n"

    with open(fname, "a") as f:
        f.write(record)

    sync_route_files()
    print(f"Record for {name} ({sid}) saved successfully.")

def display_students():
    print("\n--- Display Section Records ---")
    c_name = input("Enter Class: ").strip()
    s_name = input("Enter Section: ").strip().upper()
    fname = get_student_file(c_name, s_name)

    if not os.path.exists(fname):
        print("No records found for this class and section.")
        return

    with open(fname, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No student records exist in this section.")
        return

    print("=" * 80)
    for line in lines:
        if not line.strip():
            continue
        p = line.strip().split("|")
        p_name, p_contact, p_job = p[6].split(";")  
        pct_display = f"{p[11]}%" if p[11] != "N/A" else "N/A"
        print(f"ID: {p[0]} | Name: {p[1]} | DOB: {p[2]} | Class: {p[3]}-{p[4]} | Contact: {p[5]}")
        print(f"Email: {p[7]} | Parent: {p_name} ({p_job}) - Contact: {p_contact} | Transport: {p[8]}")
        print(f"Subjects & Marks: {p[9]}")
        print(f"Average: {p[10]} | Percentage: {pct_display} | Overall Grade: {p[12]}")
        print("-" * 80)

def modify_student():
    print("\n--- Modify Student Record ---")
    c_name = input("Enter Current Class: ").strip()
    s_name = input("Enter Current Section: ").strip().upper()
    fname = get_student_file(c_name, s_name)

    if not os.path.exists(fname):
        print("Record file does not exist.")
        return

    sid = format_student_id(input("Enter Student ID to modify: "))
    updated_record = None
    remaining_lines = []

    with open(fname, "r") as f:
        lines = f.readlines()

    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split("|")
        if parts[0] == sid:
            print(f"Editing record for: {parts[1]}")
            parts[1] = input(f"New Name [{parts[1]}]: ").strip() or parts[1]
            parts[2] = input(f"New DOB [{parts[2]}]: ").strip() or parts[2]

            new_c = input(f"New Class [{parts[3]}]: ").strip() or parts[3]
            new_s = input(f"New Section [{parts[4]}]: ").strip().upper() or parts[4]
            parts[3] = new_c
            parts[4] = new_s

            parts[5] = input(f"New Contact [{parts[5]}]: ").strip() or parts[5]
            parts[7] = input(f"New Email [{parts[7]}]: ").strip() or parts[7]

            change_t = input(f"Change Transport Mode? Current [{parts[8]}] (y/n): ").strip().lower()
            if change_t == 'y':
                parts[8] = select_transport_option()

            updated_record = parts
        else:
            remaining_lines.append(line)

    if updated_record:
        target_fname = get_student_file(updated_record[3], updated_record[4])
        if target_fname == fname:
            remaining_lines.append("|".join(updated_record) + "\n")
            with open(fname, "w") as f:
                f.writelines(remaining_lines)
        else:
            with open(fname, "w") as f:
                f.writelines(remaining_lines)
            with open(target_fname, "a") as f:
                f.write("|".join(updated_record) + "\n")
        sync_route_files()
        print("Record successfully updated.")
    else:
        print("Student ID not found in this section.")

def delete_student():
    print("\n--- Delete Student Record ---")
    c_name = input("Enter Class: ").strip()
    s_name = input("Enter Section: ").strip().upper()
    fname = get_student_file(c_name, s_name)

    if not os.path.exists(fname):
        print("File does not exist.")
        return

    sid = format_student_id(input("Enter Student ID to delete: "))
    deleted = False
    new_lines = []

    with open(fname, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                if parts[0] == sid:
                    deleted = True
                else:
                    new_lines.append(line)

    if deleted:
        with open(fname, "w") as f:
            f.writelines(new_lines)
        sync_route_files()
        print("Record deleted successfully.")
    else:
        print("Student ID not found.")

def student_menu():
    while True:
        print("\n--- STUDENT & GRADES MODULE ---")
        print("1. Add New Student")
        print("2. View Students by Class & Section")
        print("3. Modify Student Information")
        print("4. Delete Student Record")
        print("5. Return to Main Menu")
        ch = input("Choose (1-5): ").strip()
        if ch == "1":
            add_student()
        elif ch == "2":
            display_students()
        elif ch == "3":
            modify_student()
        elif ch == "4":
            delete_student()
        elif ch == "5":
            break
        else:
            print("Invalid input.")
