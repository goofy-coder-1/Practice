import csv
import os

class Student:
    """Represents an individual student."""
    def __init__(self, name, address, age, student_id, grade):
        self.name = name
        self.address = address
        self.age = age
        self.student_id = student_id
        self.grade = grade

    def display_details(self):
        print("\n------ Student Details ---------")
        print(f"Name:        {self.name}")
        print(f"Address:     {self.address}")
        print(f"Age:         {self.age}")
        print(f"Student ID:  {self.student_id}")
        print(f"Grade/Class: {self.grade}")
        print("--------------------------------\n")


class StudentDatabase:
    """Handles all File I/O operations for students using OOP principles."""
    CSV_FILE = "student_database.csv"

    @classmethod
    def check_if_exists(cls, name, student_id):
        """Checks if a student already exists by checking Name or Student ID."""
        if not os.path.exists(cls.CSV_FILE):
            return False

        with open(cls.CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            
            for row in reader:
                if row:
                    # Check unique Student ID (index 3) or Exact Name (index 0)
                    if (row[3].strip() == str(student_id).strip() or 
                        row[0].strip().lower() == name.strip().lower()):
                        return True
        return False
    
    @classmethod
    def save_to_csv(cls, student):
        """Appends the student object's data into the CSV file."""
        file_exists = os.path.exists(cls.CSV_FILE)

        # Fix: Ensure headers exactly match the 5 properties we are saving
        headers = ["Name", "Address", "Age", "StudentID", "Grade"]

        with open(cls.CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(headers)
                
            writer.writerow([
                student.name, 
                student.address, 
                student.age, 
                student.student_id, 
                student.grade
            ])
        print(f"Successfully saved {student.name} to database!")

# --- Quick Test ---
if __name__ == "__main__":
    # Create a new student object
    new_student = Student("Alice Smith", "123 Maple St", 15, "STU101", "10th Grade")
    
    # Check if they exist, if not, save them
    if not StudentDatabase.check_if_exists(new_student.name, new_student.student_id):
        StudentDatabase.save_to_csv(new_student)
    else:
        print("Student already exists in the database!")
        
    new_student.display_details()