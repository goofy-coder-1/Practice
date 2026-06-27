import csv
import os
from datetime import datetime
from functions import fetch_student_brief

MASTER_ID = "OWNER123"  
PAYMENT_FILE = "payment_base.csv"

def verify_owner():
    entered_id = input("Enter Owner/Master ID: ").strip()
    return entered_id == MASTER_ID


# FEATURE 1: View entire payment history for a specific student
def check_payment_status(student_id):
    if not verify_owner():
        print("[ACCESS DENIED] Invalid Master ID.")
        return

    if not os.path.exists(PAYMENT_FILE):
        print("\n[INFO] No payment history file found yet. (No payments made).")
        return

    print(f"\n=== Payment History for Student ID: {student_id} ===")
    found = False
    
    with open(PAYMENT_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        
        for row in reader:
            if row and row[0].strip() == str(student_id).strip():
                # Format: StudentID[0], Name[1], Month[2], Year[3], Timestamp[4], Status[5]
                print(f"Month: {row[2]} {row[3]} | Paid On: {row[4]} | Status: {row[5]}")
                found = True
                
    if not found:
        print("No payment records found for this student.")
    print("===============================================\n")


# FEATURE 2: Add a new payment record to the ledger
def update_payment_status(student_id):
    if not verify_owner():
        print("[ACCESS DENIED] Invalid Master ID.")
        return

    # Check if student exists in student_base.csv first
    student = fetch_student_brief(student_id)
    if not student:
        print("[ERROR] Cannot log payment. Student ID does not exist in registry.")
        return

    print(f"\nLogging payment for: {student['name']}")
    month = input("Enter target month (e.g., January): ").strip().capitalize()
    year = input("Enter target year (e.g., 2026): ").strip()
    
    # Capture the exact date and time right now
    exact_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(PAYMENT_FILE)

    with open(PAYMENT_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Create headers if file is brand new
        if not file_exists:
            writer.writerow(["StudentID", "Name", "Month", "Year", "Date_Paid", "Status"])
            
        writer.writerow([
            student_id,
            student['name'],
            month,
            year,
            exact_time,
            "Paid"
        ])
        
    print(f"[SUCCESS] Recorded payment for {student['name']} for {month} {year}.")