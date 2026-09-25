"""
fee.py
Module 5: Student fee slab categorization and scholarship eligibility.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import (
    format_student_id,
    get_student_file,
    student_exists_anywhere,
    sync_route_files,
    select_transport_option
)

import os
from utils import format_student_id, get_student_file

def get_fee_category(pct):
    scholarship = False
    if pct >= 96:
        scholarship = True
        cat = 1
    elif pct >= 85:
        cat = 1
    elif pct >= 70:
        cat = 2
    elif pct >= 55:
        cat = 3
    elif pct >= 40:
        cat = 4
    else:
        cat = 5
    return cat, scholarship

def view_fee_category():
    print("\n--- Student Fee Category Lookup ---")
    c_name = input("Enter Student Class: ").strip()
    s_name = input("Enter Student Section: ").strip().upper()
    fname = get_student_file(c_name, s_name)

    if not os.path.exists(fname):
        print("Record file does not exist.")
        return

    sid = format_student_id(input("Enter Student ID: "))
    found = False

    with open(fname, "r") as f:
        for line in f:
            if line.strip():
                p = line.strip().split("|")
                if p[0] == sid:
                    found = True
                    if p[11] == "N/A":
                        print(f"\nMarks/Percentage not yet recorded for {p[1]} (ID: {sid}). Fee category cannot be computed.")
                        break

                    pct = float(p[11])
                    grade = p[12]
                    cat, scholarship = get_fee_category(pct)

                    print("\n" + "=" * 45)
                    print(f"Fee Profile for: {p[1]} (ID: {sid})")
                    print(f"Total Percentage: {pct}% | Overall Grade: {grade}")
                    print(f"Assigned Fee Category: Category {cat}")
                    print(f"Scholarship Status: {'ELIGIBLE (96% - 100%)' if scholarship else 'Not Applicable'}")
                    print("=" * 45)
                    break

    if not found:
        print("Student ID not found in this section.")

def display_all_fee_categories():
    print("\n--- Section-wide Fee Categories ---")
    c_name = input("Enter Class: ").strip()
    s_name = input("Enter Section: ").strip().upper()
    fname = get_student_file(c_name, s_name)

    if not os.path.exists(fname):
        print("Section not found.")
        return

    print("=" * 65)
    print(f"{'ID':<10}{'Name':<20}{'Pct':<8}{'Grade':<8}{'Category':<10}{'Scholarship'}")
    print("-" * 65)
    with open(fname, "r") as f:
        for line in f:
            if line.strip():
                p = line.strip().split("|")
                if p[11] == "N/A":
                    print(f"{p[0]:<10}{p[1]:<20}{'N/A':<8}{'N/A':<8}{'Pending':<10}No")
                else:
                    pct = float(p[11])
                    grade = p[12]
                    cat, sch = get_fee_category(pct)
                    sch_txt = "Yes" if sch else "No"
                    print(f"{p[0]:<10}{p[1]:<20}{pct:<8}{grade:<8}{'Cat ' + str(cat):<10}{sch_txt}")
    print("=" * 65)

def fee_menu():
    while True:
        print("\n--- FEES CATEGORY MODULE ---")
        print("1. Search Fee Category by Student ID")
        print("2. Display All Fee Categories for a Section")
        print("3. Return to Main Menu")
        ch = input("Choose (1-3): ").strip()
        if ch == "1":
            view_fee_category()
        elif ch == "2":
            display_all_fee_categories()
        elif ch == "3":
            break
        else:
            print("Invalid input.")
