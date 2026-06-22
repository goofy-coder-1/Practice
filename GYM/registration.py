import csv
import os
from datetime import datetime  # <-- Add this at the very top of user_base.py

class Userdetail:
    # Add an optional date parameter (defaults to today)
    def __init__(self, name, address, age, height, weight, date_recorded=None):
        self.name = name
        self.address = address
        self.age = age
        self.height = height
        self.weight = weight
        # If no date is given, use today's date in YYYY-MM-DD format
        self.date_recorded = date_recorded if date_recorded else datetime.today().strftime('%Y-%m-%d')
    
    def displayDetails(self):
        print("\n------ Your Details ---------")
        print(f"Date Logged:     {self.date_recorded}")  # <-- Added date display
        print(f"Name:            {self.name}")
        print(f"Address:         {self.address}")
        print(f"Age:             {self.age}")
        print(f"Height:          {self.height} cm")
        print(f"Current Weight:  {self.weight} kg")
        print("-----------------------------\n")

class userBase:
    CSV_FILE = "bodybuilders.csv"

    # ... keep existence_checking as it is ...

    @classmethod
    def save_to_csv(cls, account):
        file_exits = os.path.exists(cls.CSV_FILE)

        with open(cls.CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Updated header to include Date
            if not file_exits:
                writer.writerow(["Name", "Address", "Age", "Height", "Weight", "Date Recorded"])

            # Save the date along with the user specs
            writer.writerow([
                account.name,
                account.address,
                account.age,
                account.height,
                account.weight,
                account.date_recorded
            ])
            
    @classmethod
    def update_user_weight(cls, name, new_weight):
        """Finds the most recent profile info for a user and appends a new weight log."""
        user = cls.fetch_user_details(name)
        if not user:
            return False
        
        # Create a new entry copy with the updated weight
        updated_entry = Userdetail(user.name, user.address, user.age, user.height, new_weight)
        cls.save_to_csv(updated_entry)
        return True

    @classmethod
    def fetch_user_details(cls, name):
        """Searches the CSV and returns the LATEST logged entry for a user."""
        if not os.path.exists(cls.CSV_FILE):
            return None

        latest_match = None
        with open(cls.CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None) 
            
            for row in reader:
                if row and row[0].strip().lower() == name.strip().lower():
                    # Keep overwriting latest_match so we return the most recent row at the bottom
                    latest_match = Userdetail(row[0], row[1], row[2], row[3], row[4], row[5])
                    
        return latest_match