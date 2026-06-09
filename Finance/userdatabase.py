from accountnum import numbergeneration

def NewUser():
    try:
        Name = input("Enter your name: ")
        Address = input("Enter the address: ")
        Age = input("Enter your age: ")
        Pin = int(input("Set your PIN (numbers only): "))

        # Generate the account number only after successful inputs
        accountNum = numbergeneration()
        
        print("\n------ Your Details ---------")
        print(f"Name: {Name}")
        print(f"Address: {Address}")
        print(f"Account Number: {accountNum}")
        print("-----------------------------\n")

        
        return Name, Address, Age, Pin, accountNum
        
    except ValueError:
        print("\nInput error detected! Please ensure your PIN is a number.\n")

if __name__ == "__main__":
    NewUser()