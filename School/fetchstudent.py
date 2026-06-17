import json
import os
from datetime import datetime

def add_exam_records():
    print("\n---- Exam Perfomance Detail ----")
    student_id = input("Enter Student ID: ").strip().upper()
    exam_name = input("Enter Exam Name (e.g., Midterm, Final): ").strip()
    subject = input("Enter Subject: ").strip()

    while True:
        try:
            score = float(input("Enter Score/Percentage: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical score.")

    new_record = {
        "exam_name": exam_name,
        "subject": subject,
        "score": score,
        "date_recorded": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    json_file = "performance_history.json"
    database = {}

    if os.path.exists(json_file):
        try:
            with open(json_file, "r", encoding='utf-8') as file:
                database = json.load(file)
        except json.JSONDecodeError:
            database = {}
    
    if student_id in database:
        database[student_id].append(new_record)
    else:
        database[student_id] = [new_record]

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(database, file, indent=4)

    print(f"\n Exam record successfully saved for Student ID: {student_id}!")

if __name__ == "__main__":
    while True:
        add_exam_records()
        cont = input("\nDo you want to add another exam record? (y/n): ").strip().lower()
        if cont != 'y':
            break