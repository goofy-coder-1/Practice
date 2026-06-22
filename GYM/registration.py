import csv
import os

class Userdetail:
    def __init__(self, name, address, age, height, weight):
        self.name = name
        self.address = address
        self.age - age
        self.height = height
        self.weight = weight
    
    def displayDetails(self):
        print("\n------ Your Details ---------")
        print(f"Name:            {self.name}")
        print(f"Address:         {self.address}")
        print(f"Age:             {self.age}")
        print(f"Height:  {self.height}")
        print(f"Current Weight: {self.weight}")
        print("-----------------------------\n")

class userBase:
    CSV_FILE = "bodybuilders.csv"

    @classmethod
    def existence_checking(cls, name, address, age):
        if not os.path.exists(cls.CSV_FILE):
            return 0
    
        with open(cls.CSV_FILE, mode = "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
               if (row[0].strip().lower() == name.strip().lower() and 
                        row[1].strip().lower() == address.strip().lower() and 
                        row[2].strip() == str(age).strip()):
                        return True
        return False
    
    @classmethod
    def save_to_csv()