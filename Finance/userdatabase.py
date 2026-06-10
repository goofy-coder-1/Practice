import csv
import os
from accountnum import AccountGenerator

class BankAccount:
    def __init__(self, name, address, age, pin, capital):
        self.name = name
        self.address = address
        self.age = age
        self.pin = pin
        self.capital = capital
        self.account_number = AccountGenerator.generate_number()

    def display_details(self):
        print("\n------ Your Details ---------")
        print(f"Name:            {self.name}")
        print(f"Address:         {self.address}")
        print(f"Age:             {self.age}")
        print(f"Account Number:  {self.account_number}")
        print(f"Current Capital: {self.capital}")
        print("-----------------------------\n")


class BankSystem:
    CSV_FILE = "bank_accounts.csv"

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
                    # Compare Name, Address, and Age (case-insensitive for text fields)
                    if (row[0].strip().lower() == name.strip().lower() and 
                        row[1].strip().lower() == address.strip().lower() and 
                        row[2].strip() == str(age).strip()):
                        return True
        return False

    @classmethod
    def save_to_csv(cls, account):
        """Appends the account object's data into the CSV file."""
        file_exists = os.path.exists(cls.CSV_FILE)

        with open(cls.CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # If the file is brand new, write the headers first
            if not file_exists:
                writer.writerow(["Name", "Address", "Age", "PIN", "Capital", "Account Number"])
                
            # Write the user details
            writer.writerow([
                account.name, 
                account.address, 
                account.age, 
                account.pin, 
                account.capital, 
                account.account_number
            ])

    @classmethod
    def register_new_user(cls):
        try:
            name = input("Enter your name: ")
            address = input("Enter the address: ")
            age = input("Enter your age: ")
            
            if cls.check_if_exists(name, address, age):
                print("\nRegistration Failed: Data already exists in the system!")
                return None

            pin = int(input("Set your PIN (numbers only): "))
            capital = int(input("Initial Capital to be deposited: "))

           
            user_account = BankAccount(name, address, age, pin, capital)
            
            
            user_account.display_details()
            
            
            confirmation = input("Do you want to save these details? (yes/no): ").strip().lower()
            
            if confirmation in ["yes", "y"]:
                cls.save_to_csv(user_account)
                print("Account successfully created and recorded in database!")
                return user_account
            else:
                print("Registration cancelled by user. Data was not saved.")
                return None

        except ValueError:
            print("\nInput error detected! Please ensure your PIN and Capital are numbers.\n")
            return None


if __name__ == "__main__":
    active_account = BankSystem.register_new_user()