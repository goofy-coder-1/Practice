import csv
import os

class BankAccount:
    def __init__(self, name, address, age, grade, contact):
        self.name = name
        self.address = address
        self.age = age
        self.grade = grade
        self.contact = contact

    def display_details(self):
        print("\n------ Your Details ---------")
        print(f"Name:            {self.name}")
        print(f"Address:         {self.address}")
        print(f"Age:             {self.age}")
        print(f"Account Number:  {self.grade}")
        print(f"Current Capital: {self.contact}")
        print("-----------------------------\n")

class StudentDatabase:
    CSV_FILE = "student_database.csv"

    @classmethod
    def check_if_exists(cls, name, address, age):
        """Reads the CSV file to check if a user with the same core details exists."""
        if not os.path.exists(cls.CSV_FILE):
            return False

        with open(cls.CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  
            
            for row in reader:
                if row:
                   
                    if (row[0].strip().lower() == name.strip().lower() and 
                        row[1].strip().lower() == address.strip().lower() and 
                        row[2].strip() == str(age).strip()):
                        return True
        return False
