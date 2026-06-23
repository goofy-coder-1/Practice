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

class studentDetail:
    
    def __init__(self, name, age, address, room_number, Level):
        self.name = name
        self.age = age
        self.address = address
        self.room_number = room_number
        self.Level = Level
        self.student_id = AccountGenerator.generate_number()

    def displayDetails(self):
        print("\n------ Student Details ---------")
        print(f"Name:            {self.name}")
        print(f"Age:         {self.age}")
        print(f"Address:             {self.address}")
        print(f"Room Number:          {self.room_number} cm")
        print(f"Level of Study:  {self.Level} kg")
        print(f"Student ID: {self.student_id}")
        print("-----------------------------\n")

class StudentBase:
    CSV_FILE = "student_base.csv"

    @classmethod
    def existence_checking(cls, name, age, address):
        if not os.path.exists(cls.CSV_FILE):
            return False
        
        with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)

        for row in reader:
            if row:
                if(row[0].strip().lower() == name.strip().lower() and 
                    row[1].strip().lower() == address.strip().lower() and 
                        row[2].strip() == str(age).strip()):
                        return True
        return False
    
    @classmethod
    def saving_csv(cls, account):
        file_exists = os.path.exists(cls.CSV_FILE)

        with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Age", "Address", "Room_Number", "Level", "StudentID"])
            
            writer.writerow([
                account.name,
                account.age,
                account.address,
                account.room_number,
                account.Level,
                account.student_id
            ])
        
    @classmethod
    def new_student(cls):
        try:
            name = input("Enter name of student: ")
            age = input("Enter age of student: ")
            address = input("Enter address of student: ")

            if cls.existence_checking(name, age, address):
                print("Registration failed as system already has given detail")
                return None
            
            room_number = input("Room number: ")
            Level = input("Students level of study: ")
            
            student_account = studentDetail(name, age, address, room_number, Level)
            student_account.displayDetails()
            confirmation = input("Do you want to save these details? (yes/no): ").strip().lower()
            
            if confirmation in ["yes", "y"]:
                cls.saving_csv(student_account)
                print("Account successfully created and recorded in database!")
                return student_account
            else:
                print("Registration cancelled by user. Data was not saved.")
                return None

        except ValueError:
            print("\nInput error detected!\n")
            return None


if __name__ == "__main__":
    active_account = StudentBase.new_student()
        
                
