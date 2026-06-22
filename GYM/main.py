from registration import userBase

def main_menu():
    while True:
        print("\n=== BODYBUILDER DATABASE SYSTEM ===")
        print("1. Register a New User")
        print("2. Fetch Existing User Details (Latest)")
        print("3. Log New Weight (Append Update)")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print("\n--- Starting Registration ---")
            userBase.register_new_user()
            
        elif choice == "2":
            print("\n--- Fetch User Details ---")
            search_name = input("Enter name to look up: ")
            user = userBase.fetch_user_details(search_name)
            if user:
                user.displayDetails()
            else:
                print(f"\nError: No record found for '{search_name}'.")
                
        elif choice == "3":
            print("\n--- Update Weight Log ---")
            search_name = input("Enter user's name: ")
            
            
            user = userBase.fetch_user_details(search_name)
            if user:
                print(f"Current recorded weight for {user.name} is {user.weight} kg.")
                try:
                    new_weight = int(input("Enter new weight in Kg: "))
                    if userBase.update_user_weight(search_name, new_weight):
                        print(f"Successfully appended new weight record for {user.name}!")
                except ValueError:
                    print("Error: Weight must be a number.")
            else:
                print(f"Error: User '{search_name}' does not exist.")
                
        elif choice == "4":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()