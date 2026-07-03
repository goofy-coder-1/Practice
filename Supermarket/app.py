from service import SupermarketService


class SupermarketApp:
    """Main application controller - handles UI and user interactions"""
    
    def __init__(self):
        self.service = SupermarketService()
    
    def display_main_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("SUPERMARKET MANAGEMENT SYSTEM")
        print("="*50)
        print("\n1. INVENTORY MANAGEMENT")
        print("   1.1 - Add Product")
        print("   1.2 - View All Products")
        print("   1.3 - View Product Details")
        print("   1.4 - Update Product")
        print("   1.5 - Delete Product")
        print("   1.6 - Search Products")
        print("   1.7 - View by Category")
        print("   1.8 - View Low Stock Items")
        print("\n2. SHOPPING CART")
        print("   2.1 - Add to Cart")
        print("   2.2 - View Cart")
        print("   2.3 - Remove from Cart")
        print("   2.4 - Clear Cart")
        print("   2.5 - Checkout")
        print("\n3. Exit")
        print("="*50)
    
    def handle_inventory_menu(self, choice: str):
        """Handle inventory management operations"""
        if choice == "1.1":
            self.service.add_product()
        elif choice == "1.2":
            self.service.view_all_products()
        elif choice == "1.3":
            self.service.view_product()
        elif choice == "1.4":
            self.service.update_product()
        elif choice == "1.5":
            self.service.delete_product()
        elif choice == "1.6":
            self.service.search_products()
        elif choice == "1.7":
            self.service.view_by_category()
        elif choice == "1.8":
            self.service.view_low_stock()
        else:
            print("Invalid choice. Please try again.")
    
    def handle_cart_menu(self, choice: str):
        """Handle shopping cart operations"""
        if choice == "2.1":
            self.service.add_to_cart()
        elif choice == "2.2":
            self.service.view_cart()
        elif choice == "2.3":
            self.service.remove_from_cart()
        elif choice == "2.4":
            self.service.clear_cart()
        elif choice == "2.5":
            self.service.checkout()
        else:
            print("Invalid choice. Please try again.")
    
    def run(self):
        """Run the application with interactive menu"""
        print("\n" + "="*50)
        print("Welcome to Supermarket Management System!")
        print("="*50)
        
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice.startswith("1."):
                self.handle_inventory_menu(choice)
            elif choice.startswith("2."):
                self.handle_cart_menu(choice)
            elif choice == "3":
                print("\nThank you for using Supermarket Management System!")
                break
            else:
                print("Invalid choice. Please try again.")