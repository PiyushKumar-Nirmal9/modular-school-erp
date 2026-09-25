"""
transport.py
Module 4: Transportation routes, bus tracking, and enrollment sync.
"""

import os
from config import TRANSPORT_FILE
from utils import extract_route_number, sync_route_files

def add_route():
    print("\n--- Create Transport Route ---")
    raw_r = input("Route Number / Name (e.g. Route-1, 2): ").strip()
    r_num = extract_route_number(raw_r)
    if not r_num:
        print("Error: Route must contain a valid number.")
        return

    route_no = f"Route-{r_num}"
    bus_no = input("Bus Number: ").strip()
    driver = input("Driver Name: ").strip()
    contact = input("Driver Contact: ").strip()

    with open(TRANSPORT_FILE, "a") as f:
        f.write(f"{route_no}|{bus_no}|{driver}|{contact}\n")

    sync_route_files()
    print(f"Route {route_no} saved and individual route file created successfully.")

def view_transport_students():
    print("\n--- Students Utilizing School Transportation ---")
    sync_route_files()

    student_files = [f for f in os.listdir(".") if f.startswith("student_") and f.endswith(".txt")]
    if not student_files:
        print("No student files found.")
        return

    found = False
    print("=" * 75)
    print(f"{'ID':<10}{'Name':<20}{'Class-Sec':<12}{'Assigned Route':<18}{'Transport Mode'}")
    print("-" * 75)

    for sf in student_files:
        with open(sf, "r") as f:
            for line in f:
                if line.strip():
                    p = line.strip().split("|")
                    if len(p) > 8 and p[8].startswith("School Transportation"):
                        found = True
                        r_num = extract_route_number(p[8])
                        route_display = f"Route-{r_num}" if r_num else "Not Specified"
                        class_sec = f"{p[3]}-{p[4]}"
                        print(f"{p[0]:<10}{p[1]:<20}{class_sec:<12}{route_display:<18}School Transport")

    if not found:
        print("No students are enrolled in School Transportation.")
    print("=" * 75)

def view_route_specific_file():
    print("\n--- View Route Specific Details File ---")
    r_in = input("Enter Route Number (e.g., 1): ").strip()
    num = extract_route_number(r_in)
    fname = f"route_{num}_details.txt"

    if not os.path.exists(fname):
        print(f"File for Route {num} ({fname}) does not exist.")
        return

    with open(fname, "r") as f:
        print(f.read())

def transport_menu():
    while True:
        print("\n--- TRANSPORTATION SYSTEM ---")
        print("1. Add Route & Bus Information")
        print("2. View Students Utilizing School Transport")
        print("3. View Dedicated Route File Details")
        print("4. Return to Main Menu")
        ch = input("Choose (1-4): ").strip()
        if ch == "1":
            add_route()
        elif ch == "2":
            view_transport_students()
        elif ch == "3":
            view_route_specific_file()
        elif ch == "4":
            break
        else:
            print("Invalid input.")
