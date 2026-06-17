# search_history.py
import json
import os

def search_student_history():
    json_file = "performance_history.json"
    
    if not os.path.exists(json_file):
        print("\n No exam records found in the database yet. Add some records first!")
        return

    student_id = input("\nEnter Student ID to search: ").strip().upper()

    # Load the JSON data
    with open(json_file, "r", encoding="utf-8") as file:
        database = json.load(file)

    
    if student_id in database:
        records = database[student_id]
        print(f"\n==================================================")
        print(f"        EXAM HISTORY FOR STUDENT: {student_id}     ")
        print(f"==================================================")
        
        total_score = 0
        for idx, entry in enumerate(records, start=1):
            print(f" [{idx}] Exam:      {entry['exam_name']}")
            print(f"     Subject:   {entry['subject']}")
            print(f"     Score:     {entry['score']}%")
            print(f"     Recorded:  {entry['date_recorded']}")
            print(f"--------------------------------------------------")
            total_score += entry['score']
            
        # Fun extra feature: Calculate their historical average score
        average = total_score / len(records)
        print(f"Cumulative Average Score: {average:.2f}%")
        print(f"==================================================\n")
    else:
        print(f"\nNo performance history found for Student ID: {student_id}")

if __name__ == "__main__":
    while True:
        search_student_history()
        cont = input("Search for another student? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting search engine. Goodbye!")
            break