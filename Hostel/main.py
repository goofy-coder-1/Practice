import os
import sys

# Import functions from register.py
from register import StudentBase

# Import functions from functions.py
from functions import fetch_student_brief, delete_student, update_student_detail

# Import functions from payment.py
from payment import check_payment_status, update_payment_status, verify_owner


def display_menu():
    print("\n" + "="*40)
    print("      HOSTEL MANAGEMENT SYSTEM ADMIN     ")
    print("="*40)
    print("1. Register a New Student")
    print("2. Fetch Student Summary (ID & Name Only)")
    print("3. Modify Student Details")
    print("4. Delete Student Record (Generates Log)")
    print("5. Check Payment Status (Requires Master ID)")
    print("6. Update Payment Status (Requires Master ID)")
    print("7. Exit")
    print("="*40)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- Initializing New Student Registration ---")
            StudentBase.new_student()

        elif choice == "2":
            print("\n--- Fetch Student Brief ---")
            sid = input("Enter Student ID to search: ").strip()
            student = fetch_student_brief(sid)
            if student:
                print(f"\n[FOUND] Student ID: {student['id']} | Name: {student['name']}")
            else:
                print("\n[NOT FOUND] No student matched that ID.")

        elif choice == "3":
            print("\n--- Modify Student Profile ---")
            sid = input("Enter Student ID to modify: ").strip()
            
            # Print column guide based on your CSV row mapping
            print("\nFields you can update:")
            print("0: Name | 1: Age | 2: Address | 3: Room Number | 4: Level")
            try:
                col_idx = int(input("Enter field number to change: "))
                new_val = input("Enter new value: ").strip()
                update_student_detail(sid, col_idx, new_val)
            except ValueError:
                print("[ERROR] Field index must be a number.")

        elif choice == "4":
            print("\n--- Delete Student Record ---")
            sid = input("Enter Student ID to delete: ").strip()
            reason = input("Enter reason for deletion: ").strip()
            if not reason:
                print("[ERROR] Deletion aborted. A reason must be provided.")
                continue
            delete_student(sid, reason)

        elif choice == "5":
            print("\n--- Protected Payment Check ---")
            sid = input("Enter Student ID to inspect payment: ").strip()
            check_payment_status(sid)

        elif choice == "6":
            print("\n--- Protected Payment Status Update ---")
            sid = input("Enter Student ID logging a payment: ").strip()
            update_payment_status(sid) 

        elif choice == "7":
            print("\nThank you for using the Hostel Management System. Goodbye!")
            sys.exit()

        else:
            print("\n[INVALID CHOICE] Please choose a number between 1 and 7.")
            
        input("\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main()