"""
main.py
Application entry point and primary interactive terminal interface.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from student import student_menu
from teacher import teacher_menu
from library import library_menu
from transport import transport_menu
from fee import fee_menu
from class_analytics import class_menu

def main():
    while True:
        print("\n==========================================")
        print("        SCHOOL MANAGEMENT SYSTEM          ")
        print("==========================================")
        print("1. Student & Grade Management")
        print("2. Teacher Corner")
        print("3. Library Management System")
        print("4. School Transportation System")
        print("5. Student Fees Category")
        print("6. Class Module")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            teacher_menu()
        elif choice == "3":
            library_menu()
        elif choice == "4":
            transport_menu()
        elif choice == "5":
            fee_menu()
        elif choice == "6":
            class_menu()
        elif choice == "7":
            print("Program terminated.")
            break
        else:
            print("Invalid selection. Enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
