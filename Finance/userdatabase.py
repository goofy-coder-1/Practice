from accountnum import AccountGenerator

class BankAccount:
    def __init__(self, name, address, age, pin, capital):
        self.name = name
        self.address = address
        self.age = age
        self.pin = pin
        self.capital = capital
        
        self.account_number = AccountGenerator.generate_number()

    def displayDetails(self):
        print("\n------ Your Details ---------")
        print(f"Name:            {self.name}")
        print(f"Address:         {self.address}")
        print(f"Age:             {self.age}")
        print(f"Account Number:  {self.account_number}")
        print(f"Current Capital: {self.capital}")
        print("-----------------------------\n")

class BankSystem:
    @staticmethod
    def register_new_user():
        try:
            name = input("Enter your name: ")
            address = input("Enter the address: ")
            age = input("Enter your age: ")
            pin = int(input("Set your PIN (numbers only): "))

           
            user_account = BankAccount(name, address, age, pin)
            
          
            user_account.display_details()
            
            return user_account

        except ValueError:
            print("\nInput error detected! Please ensure your PIN is a number.\n")
            return None