import csv
import os

CSV_FILE = "student_base.csv"

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

    for row in rows:
        if len(row) > 5 and row[5].strip() == str(student_id).strip():
            student_to_delete = row
        else:
            updated_rows.append(row)

    if student_to_delete:
        _write_all_students(headers, updated_rows)
        log_filename = f"deleted_student_{student_id}.txt"
        with open(log_filename, mode='w', encoding='utf-8') as log_file:
            log_file.write(f"Deletion Log\n-------------\n")
            log_file.write(f"Student ID: {student_to_delete[5]}\n")
            log_file.write(f"Name: {student_to_delete[0]}\n")
            log_file.write(f"Reason: {reason}\n")
        print(f"[SUCCESS] Student {student_id} deleted.")
        return True
    print(f"[ERROR] Student ID {student_id} not found.")
    return False

def update_student_detail(student_id, column_index, new_value):
    headers, rows = _read_all_students()
    updated = False

    for row in rows:
        if len(row) > 5 and row[5].strip() == str(student_id).strip():
            if column_index < len(row):
                row[column_index] = new_value
                updated = True
                break

    if updated:
        _write_all_students(headers, rows)
        print(f"[SUCCESS] Updated student {student_id} profile details.")
        return True
    print(f"[ERROR] Student ID {student_id} not found.")
    return False