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
    def save_to_csv(cls, account):
        file_exits = os.path.exists(cls.CSV_FILE)

        with open(cls.CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exits:
                writer.writerow(["Name", "Address", "Age", "Height", "Weight"])

            writer.writerow([
                account.name,
                account.address,
                account.age,
                account.height,
                account.weight
            ])
    
    @classmethod
    def register_new_user(cls):
        try:
            name = input("Enter your name: ")
            address = input("Enter the address: ")
            age = input("Enter your age: ")
            
            if cls.existence_checking(name, address, age):
                print("\nRegistration Failed: Data already exists in the system!")
                return None

            height = int(input("Enter your height in cm: "))
            weight = int(input("Weight in Kg: "))

           
            user_account = Userdetail(name, address, age, height, weight)
            
            
            user_account.displayDetails()
            
            
            confirmation = input("Do you want to save these details? (yes/no): ").strip().lower()
            
            if confirmation in ["yes", "y"]:
                cls.save_to_csv(user_account)
                print("Account successfully created and recorded in database!")
                return user_account
            else:
                print("Registration cancelled by user. Data was not saved.")
                return None

        except ValueError:
            print("\nInput error detected! Please ensure your height and weight are numbers.\n")
            return None


if __name__ == "__main__":
    active_account = userBase.register_new_user()