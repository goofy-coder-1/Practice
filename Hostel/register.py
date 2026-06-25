import os
import csv
import random

class AccountGenerator:
    @staticmethod
    def generate_number():
        number_combo_first = random.randint(111, 999)
        number_combo_second = random.randint(111, 999)
        final = f"22{number_combo_first}33{number_combo_second}"
        return int(final)

class StudentDetail:
    def __init__(self, name, age, address, room_number, level):
        self.name = name
        self.age = age
        self.address = address
        self.room_number = room_number
        self.level = level
        self.student_id = AccountGenerator.generate_number()

    def display_details(self):
        print("\n------ Student Details ---------")
        print(f"Name:            {self.name}")
        print(f"Age:             {self.age}")
        print(f"Address:         {self.address}")
        print(f"Room Number:     {self.room_number}")
        print(f"Level of Study:  {self.level}")
        print(f"Student ID:      {self.student_id}")
        print("-----------------------------\n")

class StudentBase:
    CSV_FILE = "student_base.csv"

    @classmethod
    def existence_checking(cls, name, age, address):
        if not os.path.exists(cls.CSV_FILE):
            return False
        
        # Kept the loop inside the 'with' block so the file stays open while reading
        with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header

            for row in reader:
                if row:
                    
                    if (row[0].strip().lower() == name.strip().lower() and 
                        row[1].strip() == str(age).strip() and
                        row[2].strip().lower() == address.strip().lower()):
                        return True
        return False
    
    @classmethod
    def saving_csv(cls, account):
        file_exists = os.path.exists(cls.CSV_FILE)

        
        with open(cls.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Age", "Address", "Room_Number", "Level", "StudentID"])
            
            writer.writerow([
                account.name,
                account.age,
                account.address,
                account.room_number,
                account.level,
                account.student_id
            ])
        
    @classmethod
    def new_student(cls):
        try:
            name = input("Enter name of student: ").strip()
            age = input("Enter age of student: ").strip()
            address = input("Enter address of student: ").strip()

            if cls.existence_checking(name, age, address):
                print("\nRegistration failed as system already has given details.\n")
                return None
            
            room_number = input("Room number: ").strip()
            level = input("Students level of study: ").strip()
            
            student_account = StudentDetail(name, age, address, room_number, level)
            student_account.display_details()
            
            confirmation = input("Do you want to save these details? (yes/no): ").strip().lower()
            
            if confirmation in ["yes", "y"]:
                cls.saving_csv(student_account)
                print("Account successfully created and recorded in database!")
                return student_account
            else:
                print("Registration cancelled by user. Data was not saved.")
                return None

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")
            return None

if __name__ == "__main__":
    active_account = StudentBase.new_student()

#remaining will be continued tomorrow or maybe the day after tomorrow or maybe later or maybe never