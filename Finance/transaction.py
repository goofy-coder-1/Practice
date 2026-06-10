import csv
import os
import json
from datetime import datetime

try:
    from userdatabase import BankSystem
except ImportError:
    BankSystem = None

class TransactionManager:
    CSV_FILE = "bank_accounts.csv"
    JSON_FILE = "transaction_history.json"  

    @classmethod
    def _read_all_rows(cls):
        """Helper method to read all data from the CSV file."""
        if not os.path.exists(cls.CSV_FILE):
            return [], []
        
        with open(cls.CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            rows = list(reader)
        return header, rows

    @classmethod
    def _write_all_rows(cls, header, rows):
        """Helper method to rewrite the CSV file with updated data."""
        with open(cls.CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if header:
                writer.writerow(header)
            writer.writerows(rows)

    @classmethod
    def _log_transaction(cls, account_num, name, action, amount=None):
        """Helper method to log transaction events into a JSON array file."""
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "account_number": str(account_num),
            "name": name,
            "action": action
        }
        
        if amount is not None:
            log_entry["amount"] = f"Rs. {amount}"

        logs = []
        if os.path.exists(cls.JSON_FILE):
            try:
                with open(cls.JSON_FILE, "r", encoding="utf-8") as file:
                    logs = json.load(file)
            except json.JSONDecodeError:
                logs = []

        logs.append(log_entry)

        with open(cls.JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(logs, file, indent=4)

    @classmethod
    def authenticate_user(cls, account_num, pin):
        """Verifies if the account number and PIN match a record in the CSV."""
        _, rows = cls._read_all_rows()
        for row in rows:
            if row:
                if row[5].strip() == str(account_num).strip() and row[3].strip() == str(pin).strip():
                    return row
        return None

    @classmethod
    def update_account_in_csv(cls, account_num, column_index, new_value):
        """Finds a specific account and updates a specific column value."""
        header, rows = cls._read_all_rows()
        updated = False
        
        for row in rows:
            if row and row[5].strip() == str(account_num).strip():
                row[column_index] = str(new_value)
                updated = True
                break
                
        if updated:
            cls._write_all_rows(header, rows)

    @classmethod
    def start(cls):
        print("====== Welcome to the Bank Transaction Portal ======")
        user_type = input("Are you a new user or registered user? (new/registered): ").strip().lower()

        if user_type in ["new", "n"]:
            if BankSystem:
                print("\nRedirecting to User Registration...\n")
                BankSystem.register_new_user()
            else:
                print("\nRegistration system unavailable. Please run the main script.")
            return

        elif user_type in ["registered", "reg", "r"]:
            try:
                acc_num = input("Enter your Account Number: ").strip()
                pin = input("Enter your PIN: ").strip()
                
                # Authenticate customer
                user_row = cls.authenticate_user(acc_num, pin)
                
                if user_row:
                    print(f"\nAuthentication Successful! Welcome back, {user_row[0]}.")
                    cls.transaction_menu(acc_num)
                else:
                    print("\nInvalid Account Number or PIN. Access Denied.")
            except Exception as e:
                print(f"\nAn error occurred during authentication: {e}")
        else:
            print("\nInvalid choice. Exiting portal.")

    @classmethod
    def transaction_menu(cls, account_num):
        while True:
            _, rows = cls._read_all_rows()
            user_row = next(row for row in rows if row and row[5].strip() == str(account_num).strip())
            
            print("\n--- Transaction Menu ---")
            print("1. View Details (Security Masked)")
            print("2. Deposit Capital")
            print("3. Withdraw Capital")
            print("4. Change PIN")
            print("5. Exit")
            
            choice = input("Select an option (1-5): ").strip()

            if choice == "1":
                print("\n------ Your Account Details ------")
                print(f"Name:            {user_row[0]}")
                print(f"Address:         {user_row[1]}")
                print(f"Age:             {user_row[2]}")
                print(f"Current Capital: Rs. {user_row[4]}")
                print(f"Account Number:  {user_row[5]}")
                print("----------------------------------")

            elif choice == "2":
                try:
                    amount = int(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                    
                    current_capital = int(user_row[4])
                    new_capital = current_capital + amount
                    
                    cls.update_account_in_csv(account_num, column_index=4, new_value=new_capital)
                    cls._log_transaction(account_num, user_row[0], "Deposit", amount)
                    
                    print(f"Successfully deposited Rs. {amount}. New Balance: Rs. {new_capital}")
                except ValueError:
                    print("Invalid amount format.")

            elif choice == "3":
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                    
                    current_capital = int(user_row[4])
                    if amount > current_capital:
                        print(f"Insufficient Funds! Your balance is Rs. {current_capital}")
                    else:
                        new_capital = current_capital - amount
                        cls.update_account_in_csv(account_num, column_index=4, new_value=new_capital)
                        cls._log_transaction(account_num, user_row[0], "Withdrawal", amount)
                        
                        print(f"Successfully withdrew Rs. {amount}. Remaining Balance: Rs. {new_capital}")
                except ValueError:
                    print("Invalid amount format.")

            elif choice == "4":
                try:
                    new_pin = int(input("Enter your new numeric PIN: "))
                    confirm_pin = int(input("Confirm your new PIN: "))
                    
                    if new_pin != confirm_pin:
                        print("PIN mismatch! Operation aborted.")
                    else:
                        cls.update_account_in_csv(account_num, column_index=3, new_value=new_pin)
                        cls._log_transaction(account_num, user_row[0], "PIN Change")
                        
                        print("PIN updated successfully!")
                except ValueError:
                    print("PIN must be a valid number string.")

            elif choice == "5":
                print("\nThank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose options between 1 and 5.")


if __name__ == "__main__":
    TransactionManager.start()