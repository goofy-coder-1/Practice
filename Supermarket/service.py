from typing import Optional, List
from structure import Product, ShoppingCart
from repository import ProductRepository


class SupermarketService:
    """Handles business logic and operations"""
    
    def __init__(self):
        self.repository = ProductRepository()
        self.cart = ShoppingCart()
    
    @staticmethod
    def validate_product_input(product_id: str, name: str, category: str, 
                               price: float, quantity: int) -> bool:
        """Validate product input"""
        if not product_id.strip() or not name.strip() or not category.strip():
            print("Error: Product ID, name, and category cannot be empty!")
            return False
        
        if price <= 0:
            print("Error: Price must be greater than 0!")
            return False
        
        if quantity < 0:
            print("Error: Quantity cannot be negative!")
            return False
        
        return True
    
    # ============= PRODUCT MANAGEMENT =============
    
    def add_product(self) -> Optional[Product]:
        """Add a new product to inventory"""
        try:
            print("\n" + "="*50)
            print("ADD NEW PRODUCT")
            print("="*50)
            
            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()
            category = input("Enter category (e.g., Fruits, Dairy, etc.): ").strip()
            
            try:
                price = float(input("Enter price ($): "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Error: Price must be a number and quantity must be an integer!")
                return None
            
            if not self.validate_product_input(product_id, name, category, price, quantity):
                return None
            
            # Check if product ID already exists
            if self.repository.get_by_id(product_id):
                print(f"Error: Product ID '{product_id}' already exists!")
                return None
            
            product = Product(product_id, name, category, price, quantity)
            product.display()
            
            confirmation = input("\nAdd this product? (yes/no): ").strip().lower()
            
            if confirmation in ["yes", "y"]:
                if self.repository.save(product):
                    print("✓ Product successfully added!")
                    return product
                else:
                    print("✗ Failed to add product.")
                    return None
            else:
                print("Operation cancelled.")
                return None
        except Exception as e:
            print(f"Error adding product: {e}")
            return None
    
    def view_all_products(self):
        """View all products in inventory"""
        products = self.repository.get_all()
        
        if not products:
            print("\n✗ No products in inventory!")
            return
        
        print("\n" + "="*70)
        print(f"INVENTORY ({len(products)} products)")
        print("="*70)
        print(f"{'ID':<8} {'Name':<20} {'Category':<12} {'Price':>8} {'Stock':>8}")
        print("-"*70)
        
        for product in products:
            status = "OUT" if product.is_out_of_stock() else ""
            print(f"{product.product_id:<8} {product.name:<20} {product.category:<12} ${product.price:>7.2f} {product.quantity:>7} {status}")
        
        print("="*70)
    
    def view_product(self):
        """View details of a specific product"""
        print("\n" + "="*50)
        print("VIEW PRODUCT DETAILS")
        print("="*50)
        
        product_id = input("Enter product ID: ").strip()
        
        if not product_id:
            print("Error: Product ID cannot be empty!")
            return
        
        product = self.repository.get_by_id(product_id)
        
        if product:
            product.display()
        else:
            print(f"✗ Product '{product_id}' not found.")
    
    def update_product(self):
        """Update an existing product"""
        print("\n" + "="*50)
        print("UPDATE PRODUCT")
        print("="*50)
        
        product_id = input("Enter product ID to update: ").strip()
        
        if not product_id:
            print("Error: Product ID cannot be empty!")
            return
        
        product = self.repository.get_by_id(product_id)
        
        if not product:
            print(f"✗ Product '{product_id}' not found.")
            return
        
        print("\nCurrent details:")
        product.display()
        
        print("\nEnter new details (or press Enter to keep current):")
        name = input("New name: ").strip() or product.name
        category = input("New category: ").strip() or product.category
        
        try:
            price_input = input(f"New price (current ${product.price:.2f}): ").strip()
            price = float(price_input) if price_input else product.price
            
            quantity_input = input(f"New quantity (current {product.quantity}): ").strip()
            quantity = int(quantity_input) if quantity_input else product.quantity
        except ValueError:
            print("Error: Invalid price or quantity!")
            return
        
        if not self.validate_product_input(product_id, name, category, price, quantity):
            return
        
        updated_product = Product(product_id, name, category, price, quantity, product.added_date)
        updated_product.display()
        
        confirmation = input("\nSave changes? (yes/no): ").strip().lower()
        
        if confirmation in ["yes", "y"]:
            if self.repository.update(product_id, updated_product):
                print("✓ Product successfully updated!")
            else:
                print("✗ Failed to update product.")
        else:
            print("Operation cancelled.")
    
    def delete_product(self):
        """Delete a product from inventory"""
        print("\n" + "="*50)
        print("DELETE PRODUCT")
        print("="*50)
        
        product_id = input("Enter product ID to delete: ").strip()
        
        if not product_id:
            print("Error: Product ID cannot be empty!")
            return
        
        product = self.repository.get_by_id(product_id)
        
        if not product:
            print(f"✗ Product '{product_id}' not found.")
            return
        
        product.display()
        
        confirmation = input("\nAre you sure you want to delete this product? (yes/no): ").strip().lower()
        
        if confirmation in ["yes", "y"]:
            if self.repository.delete(product_id):
                print("✓ Product successfully deleted!")
            else:
                print("✗ Failed to delete product.")
        else:
            print("Operation cancelled.")
    
    def search_products(self):
        """Search products by name"""
        print("\n" + "="*50)
        print("SEARCH PRODUCTS")
        print("="*50)
        
        name = input("Enter product name (partial match okay): ").strip()
        
        if not name:
            print("Error: Product name cannot be empty!")
            return
        
        products = self.repository.search_by_name(name)
        
        if not products:
            print(f"✗ No products found matching '{name}'")
            return
        
        print(f"\n✓ Found {len(products)} product(s):")
        print("-"*50)
        
        for product in products:
            product.display_compact()
    
    def view_by_category(self):
        """View all products in a category"""
        print("\n" + "="*50)
        print("VIEW BY CATEGORY")
        print("="*50)
        
        category = input("Enter category name: ").strip()
        
        if not category:
            print("Error: Category cannot be empty!")
            return
        
        products = self.repository.get_by_category(category)
        
        if not products:
            print(f"✗ No products found in category '{category}'")
            return
        
        print(f"\n✓ Products in category '{category}':")
        print("-"*50)
        
        for product in products:
            product.display_compact()
    
    def view_low_stock(self):
        """View products with low stock"""
        print("\n" + "="*50)
        print("LOW STOCK ALERT")
        print("="*50)
        
        try:
            threshold = int(input("Enter stock threshold (default 5): ") or "5")
        except ValueError:
            threshold = 5
        
        products = self.repository.get_low_stock(threshold)
        
        if not products:
            print(f"✓ All products have sufficient stock (threshold: {threshold})")
            return
        
        print(f"\n⚠ {len(products)} product(s) with stock below {threshold}:")
        print("-"*50)
        
        for product in products:
            print(f"[{product.product_id}] {product.name} - Stock: {product.quantity}")
    
    # ============= SHOPPING CART OPERATIONS =============
    
    def add_to_cart(self):
        """Add product to shopping cart"""
        print("\n" + "="*50)
        print("ADD TO CART")
        print("="*50)
        
        product_id = input("Enter product ID: ").strip()
        
        if not product_id:
            print("Error: Product ID cannot be empty!")
            return
        
        product = self.repository.get_by_id(product_id)
        
        if not product:
            print(f"✗ Product '{product_id}' not found.")
            return
        
        if product.is_out_of_stock():
            print(f"✗ Product '{product.name}' is out of stock!")
            return
        
        product.display()
        
        try:
            quantity = int(input(f"Enter quantity (available: {product.quantity}): "))
        except ValueError:
            print("Error: Quantity must be an integer!")
            return
        
        if quantity <= 0:
            print("Error: Quantity must be greater than 0!")
            return
        
        if quantity > product.quantity:
            print(f"Error: Only {product.quantity} items available!")
            return
        
        if self.cart.add_item(product, quantity):
            print(f"✓ Added {quantity} x {product.name} to cart!")
        else:
            print("✗ Failed to add item to cart.")
    
    def view_cart(self):
        """View shopping cart"""
        self.cart.display()
    
    def remove_from_cart(self):
        """Remove product from shopping cart"""
        if self.cart.is_empty():
            print("\n✗ Cart is empty!")
            return
        
        print("\n" + "="*50)
        print("REMOVE FROM CART")
        print("="*50)
        
        self.view_cart()
        
        product_id = input("\nEnter product ID to remove: ").strip()
        
        if not product_id:
            print("Error: Product ID cannot be empty!")
            return
        
        if self.cart.remove_item(product_id):
            print(f"✓ Removed product from cart!")
        else:
            print(f"✗ Product '{product_id}' not found in cart.")
    
    def checkout(self):
        """Checkout shopping cart"""
        if self.cart.is_empty():
            print("\n✗ Cart is empty!")
            return
        
        self.cart.display()
        
        confirmation = input("\nProceed with checkout? (yes/no): ").strip().lower()
        
        if confirmation in ["yes", "y"]:
            # Update inventory after checkout
            for item in self.cart.items.values():
                product = self.repository.get_by_id(item.product.product_id)
                if product:
                    product.quantity -= item.quantity
                    self.repository.update(product.product_id, product)
            
            total = self.cart.get_total()
            print("\n" + "="*50)
            print("CHECKOUT SUCCESSFUL!")
            print("="*50)
            print(f"Total Amount: ${total:.2f}")
            print("Thank you for shopping with us!")
            print("="*50)
            
            self.cart.clear()
        else:
            print("Checkout cancelled.")
    
    def clear_cart(self):
        """Clear shopping cart"""
        if self.cart.is_empty():
            print("\n✗ Cart is already empty!")
            return
        
        confirmation = input("Clear entire cart? (yes/no): ").strip().lower()
        
        if confirmation in ["yes", "y"]:
            self.cart.clear()
            print("✓ Cart cleared!")
        else:
            print("Operation cancelled.")