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
    """Handles all File I/O operations for students."""
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
                    
                    if (row[3].strip().lower() == str(student_id).strip().lower() or 
                        row[0].strip().lower() == name.strip().lower()):
                        return True
        return False
    
    @classmethod
    def save_to_csv(cls, student):
        """Appends the student object's data into the CSV file."""
        file_exists = os.path.exists(cls.CSV_FILE)
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
        print(f"\nSuccessfully saved {student.name} to the database!")



def main():
    while True:
        print("\n=== STUDENT DATABASE MENU ===")
        print("1. Add a New Student")
        print("2. Exit")
        
        choice = input("Select an option (1-2): ").strip()
        
        if choice == "1":
            print("\n--- Enter Student Information ---")
            name = input("Enter Name: ").strip()
            address = input("Enter Address: ").strip()
            
           
            while True:
                try:
                    age = int(input("Enter Age: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for age.")
            
            student_id = input("Enter Student ID: ").strip()
            grade = input("Enter Grade/Class: ").strip()
            
            
            if StudentDatabase.check_if_exists(name, student_id):
                print("\nError: A student with this Name or ID already exists!")
            else:
                
                new_student = Student(name, address, age, student_id, grade)
                
               
                StudentDatabase.save_to_csv(new_student)
                new_student.display_details()
                
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    main()