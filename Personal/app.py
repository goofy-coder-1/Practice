from service import BucketListService


class BucketListApp:
    """Main application controller - handles UI and user interactions"""
    
    def __init__(self):
        self.service = BucketListService()
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*40)
        print("BUCKET LIST APPLICATION")
        print("="*40)
        print("1. Add a new place")
        print("2. View all places")
        print("3. View place details")
        print("4. Update a place")
        print("5. Delete a place")
        print("6. Exit")
        print("="*40)
    
    def run(self):
        """this person is shit"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.service.add_place()
            elif choice == "2":
                self.service.view_all_places()
            elif choice == "3":
                self.service.view_place()
            elif choice == "4":
                self.service.update_place()
            elif choice == "5":
                self.service.delete_place()
            elif choice == "6":
                print("\nThank you for using Bucket List App!")
                break
            else:
                print("Invalid choice. Please try again.")