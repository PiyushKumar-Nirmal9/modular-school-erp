"""
utils.py
Common reusable validator, formatting, and helper utilities.
"""

import os
from config import TEACHER_FILE, TRANSPORT_FILE

def format_student_id(raw_id):
    """Enforce uppercase Student ID starting with 'S'."""
    val = raw_id.strip().upper()
    if not val.startswith("S"):
        val = "S" + val
    return val

def format_teacher_id(raw_id):
    """Enforce uppercase Teacher ID starting with 'T'."""
    val = raw_id.strip().upper()
    if not val.startswith("T"):
        val = "T" + val
    return val

def extract_route_number(route_str):
    """Extracts contiguous numeric digits using standard string operations."""
    num_str = ""
    for ch in route_str:
        if ch.isdigit():
            num_str += ch
        elif num_str:
            break
    return num_str

def get_student_file(c_name, s_name):
    """Returns standard section file name based on class and section."""
    return f"student_{c_name.strip()}_{s_name.strip().upper()}.txt"

def student_exists_anywhere(sid):
    """Checks if a Student ID exists across all section files."""
    for f in os.listdir("."):
        if f.startswith("student_") and f.endswith(".txt"):
            with open(f, "r") as fl:
                for line in fl:
                    if line.strip() and line.strip().split("|")[0] == sid:
                        return True
    return False

def teacher_exists(fid):
    """Checks if a Teacher ID exists in teachers.txt."""
    if not os.path.exists(TEACHER_FILE):
        return False
    with open(TEACHER_FILE, "r") as f:
        for line in f:
            if line.strip() and line.strip().split("|")[0] == fid:
                return True
    return False

def get_registered_routes():
    """Returns a dict mapping numeric route ID to its full details."""
    routes = {}
    if os.path.exists(TRANSPORT_FILE):
        with open(TRANSPORT_FILE, "r") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split("|")
                    r_num = extract_route_number(parts[0])
                    if r_num:
                        routes[r_num] = parts
    return routes

def sync_route_files():
    """Rebuilds route_<num>_details.txt files from master route info and student files."""
    routes = get_registered_routes()
    for r_num, r_data in routes.items():
        fname = f"route_{r_num}_details.txt"
        with open(fname, "w") as rf:
            rf.write("=========================================\n")
            rf.write(f"ROUTE DETAILS: Route-{r_num}\n")
            rf.write(f"Bus Number    : {r_data[1]}\n")
            rf.write(f"Driver Name   : {r_data[2]}\n")
            rf.write(f"Driver Contact: {r_data[3]}\n")
            rf.write("=========================================\n")
            rf.write("ENROLLED STUDENTS:\n")
            rf.write(f"{'SID':<10}{'Name':<20}{'Class-Sec':<12}\n")
            rf.write("-" * 42 + "\n")

            for sf in os.listdir("."):
                if sf.startswith("student_") and sf.endswith(".txt"):
                    with open(sf, "r") as fl:
                        for line in fl:
                            if line.strip():
                                p = line.strip().split("|")
                                if len(p) > 8 and p[8].startswith("School Transportation"):
                                    assigned_num = extract_route_number(p[8])
                                    if assigned_num == r_num:
                                        rf.write(f"{p[0]:<10}{p[1]:<20}{p[3]}-{p[4]:<12}\n")

def select_transport_option():
    """Interactive route selector with existence validation."""
    routes = get_registered_routes()
    while True:
        print("\nTransportation Mode: [1] Self  [2] School Transportation")
        t_opt = input("Choice (1/2): ").strip()
        if t_opt == "1":
            return "Self"
        elif t_opt == "2":
            if not routes:
                print("No school bus routes are registered in the system yet. Defaulting to Self.")
                return "Self"
            
            print("\nAvailable Registered Routes:")
            for r_num, r_info in routes.items():
                print(f"- Route {r_num} (Bus: {r_info[1]}, Driver: {r_info[2]})")
            
            user_route = input("Enter Route Number or Name (e.g., 1, Route 1): ").strip()
            num = extract_route_number(user_route)
            
            if num in routes:
                return f"School Transportation (Route-{num})"
            else:
                print(f"Error: Route '{user_route}' does not exist. Please re-select your transportation option.")
        else:
            print("Invalid selection. Please choose 1 or 2.")
