import csv
import os
from datetime import datetime

class PersonalBucket:
    def __init__(self, name, address, reason):
        self.name = name
        self.address = address
        self.reason = reason
        self.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def displayDetails(self):
        print("\n -------- Your Details ---------")
        print(f"Name of Place      :{self.name}")
        print(f"Address of Place   :{self.address}")
        print(f"Name of Place      :{self.reason}")
        print("------------------------------------")

class personalBase:
    CSV_FILE = "bucketlist.csv"

    @classmethod
    def check_save(cls, account):
        file_exists = os.path.exists(cls.CSV_FILE)

        with open(cls.CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Address", "Reason"])

            writer.writerow([
                account.name,
                account.address,
                account.reason
            ])

    @classmethod
    def register_new_place(cls):
        try:
            name = input("Enter name of place: ")
            address = input("Enter address of place: ")
            reason = input("Reason to visit the place: ")
        
            name_detail = PersonalBucket(name, address, reason)
            name_detail.displayDetails()
            confirmation = input("Do you want to save these details? (yes/no): ").strip().lower()
                
            if confirmation in ["yes", "y"]:
                cls.check_save(name_detail)
                print("Place successfully identified and recorded in database!")
                return name_detail
            else:
                print("Registration cancelled by user. Data was not saved.")
                return None
        except ValueError:
            print("\n Input error detected \n")
            return None
        
    @classmethod
    def fetching_place_detail(cls, name):
        if not os.path.exists(cls.CSV_FILE):
            return None
        
        with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if row and row[0].strip().lower() == name.strip().lower():
                    return PersonalBucket(row[0], row[1], row[2])
        return None
    
if __name__ == "__main__":
    active_place = personalBase.register_new_place() #kina ho one contribution matra
