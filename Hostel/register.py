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
    def existence_checking(cls):
        if not os.path.exists(cls.CSV_FILE):
            return False
        
        with open(cls.CSV_FILE, mode='r', newline='utf-8')