import csv
import os

CSV_FILE = "student_base.csv"
CSV_LOG_FILE = "delete_history.csv"

def _read_all_students():
    if not os.path.exists(CSV_FILE):
        return [], []
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        try:
            headers = next(reader)
            return headers, list(reader)
        except StopIteration:
            return [], []

def _write_all_students(headers, rows):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

def fetch_student_brief(student_id):
    headers, rows = _read_all_students()
    for row in rows:
        if len(row) > 5 and row[5].strip() == str(student_id).strip():
            return {"id": row[5], "name": row[0]}
    return None

def delete_student(student_id, reason):
    headers, rows = _read_all_students()
    updated_rows = []
    student_to_delete = None

    search_id = str(student_id).strip()

    # Find the target student
    for row in rows:
        if len(row) > 5 and str(row[5]).strip() == search_id:
            student_to_delete = row
        else:
            updated_rows.append(row)

    if student_to_delete:
        # 1. Save remaining active records back to main CSV
        _write_all_students(headers, updated_rows)
        
        # 2. Check if the central log file already exists to handle headers
        log_file_exists = os.path.exists(CSV_LOG_FILE)

        # 3. Append the deleted student's data directly to the log file
        with open(CSV_LOG_FILE, mode='a', newline='', encoding='utf-8') as log_file:
            writer = csv.writer(log_file)
            
            # Write headers if the history file is brand new
            if not log_file_exists:
                writer.writerow(["StudentID", "Name", "Age", "Room_Number", "Reason_For_Deletion"])
            
            # Append the structured record
            writer.writerow([
                student_to_delete[5],  # StudentID
                student_to_delete[0],  # Name
                student_to_delete[1],  # Age
                student_to_delete[3],  # Room Number
                reason                 # Reason provided
            ])

        print(f"[SUCCESS] Student {search_id} deleted. Log appended to central CSV archive.")
        return True
        
    print(f"[ERROR] Student ID {search_id} not found.")
    return False

def update_student_detail(student_id, column_index, new_value):
    headers, rows = _read_all_students()
    updated = False

    # Force the search key to be a clean string
    search_id = str(student_id).strip()

    for row in rows:
        # Check if the row has a valid ID column
        if len(row) > 5 and str(row[5]).strip() == search_id:
            # Check if the requested index is within the actual row size
            if 0 <= column_index < len(row):
                row[column_index] = str(new_value).strip()
                updated = True
                break
            else:
                print(f"[ERROR] Invalid field number! Choose between 0 and {len(row)-1}.")
                return False

    if updated:
        _write_all_students(headers, rows)
        print(f"[SUCCESS] Updated student {search_id} profile details.")
        return True
        
    print(f"[ERROR] Student ID {search_id} not found in the database.")
    return False