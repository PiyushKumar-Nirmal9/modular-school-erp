"""
library.py
Module 3: Library catalog, book issue, and return workflow.
"""

import os
from config import BOOKS_FILE, ISSUED_FILE
from utils import (
    format_student_id,
    format_teacher_id,
    student_exists_anywhere,
    teacher_exists
)

def add_book():
    print("\n--- Add New Book ---")
    bid = input("Book ID: ").strip()
    title = input("Book Title: ").strip()
    author = input("Author: ").strip()
    qty = input("Total Copies: ").strip()

    with open(BOOKS_FILE, "a") as f:
        f.write(f"{bid}|{title}|{author}|{qty}|{qty}\n")
    print("Book added to catalogue.")

def display_books():
    print("\n--- Book Catalogue ---")
    if not os.path.exists(BOOKS_FILE):
        print("Catalogue is empty.")
        return

    with open(BOOKS_FILE, "r") as f:
        lines = f.readlines()

    print("=" * 65)
    for line in lines:
        if line.strip():
            bid, title, auth, total, avail = line.strip().split("|")
            print(f"Book ID: {bid} | Title: {title} | Author: {auth} | Total: {total} | Available: {avail}")
    print("=" * 65)

def issue_book():
    print("\n--- Issue Book ---")
    bid = input("Enter Book ID to issue: ").strip()

    if not os.path.exists(BOOKS_FILE):
        print("Catalogue is empty.")
        return

    b_type = input("Borrower Type ([1] Student / [2] Faculty): ").strip()
    if b_type == "1" or b_type.lower() == "student":
        role = "Student"
        b_id = format_student_id(input("Enter Student ID: "))
        if not student_exists_anywhere(b_id):
            print(f"Verification Failed: Student ID '{b_id}' does not exist.")
            return
    elif b_type == "2" or b_type.lower() == "faculty":
        role = "Faculty"
        b_id = format_teacher_id(input("Enter Faculty ID: "))
        if not teacher_exists(b_id):
            print(f"Verification Failed: Faculty ID '{b_id}' does not exist.")
            return
    else:
        print("Invalid borrower type.")
        return

    books = []
    found = False
    can_issue = False

    with open(BOOKS_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                if parts[0] == bid:
                    found = True
                    avail = int(parts[4])
                    if avail > 0:
                        can_issue = True
                        parts[4] = str(avail - 1)
                books.append("|".join(parts) + "\n")

    if not found:
        print("Book ID does not exist.")
        return
    if not can_issue:
        print("No available copies to issue.")
        return

    date = input("Issue Date (DD-MM-YYYY): ").strip()

    with open(BOOKS_FILE, "w") as f:
        f.writelines(books)

    with open(ISSUED_FILE, "a") as f:
        f.write(f"{bid}|{role}|{b_id}|{date}\n")

    print(f"Book '{bid}' successfully issued to {role} ID '{b_id}'.")

def return_book():
    print("\n--- Return Book ---")
    if not os.path.exists(ISSUED_FILE):
        print("No issued books on record.")
        return

    bid = input("Enter Book ID to return: ").strip()
    raw_id = input("Enter Borrower ID (Student / Faculty): ").strip().upper()
    if raw_id.startswith("S"):
        b_id = format_student_id(raw_id)
    elif raw_id.startswith("T"):
        b_id = format_teacher_id(raw_id)
    else:
        print("Invalid ID format. Must start with 'S' or 'T'.")
        return

    issued_records = []
    issue_found = False

    with open(ISSUED_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                if not issue_found and parts[0] == bid and parts[2] == b_id:
                    issue_found = True
                else:
                    issued_records.append(line)

    if not issue_found:
        print(f"Error: No active issue record found for Book ID '{bid}' under Borrower ID '{b_id}'.")
        return

    books = []
    book_found = False

    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split("|")
                    if parts[0] == bid:
                        book_found = True
                        total = int(parts[3])
                        avail = int(parts[4])
                        if avail < total:
                            parts[4] = str(avail + 1)
                    books.append("|".join(parts) + "\n")

    with open(ISSUED_FILE, "w") as f:
        f.writelines(issued_records)

    if book_found:
        with open(BOOKS_FILE, "w") as f:
            f.writelines(books)

    print(f"Book '{bid}' returned successfully by Borrower '{b_id}'. Inventory updated.")

def library_menu():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Return to Main Menu")
        ch = input("Choose (1-5): ").strip()
        if ch == "1":
            add_book()
        elif ch == "2":
            display_books()
        elif ch == "3":
            issue_book()
        elif ch == "4":
            return_book()
        elif ch == "5":
            break
        else:
            print("Invalid input.")
