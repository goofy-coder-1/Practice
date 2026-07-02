from datetime import datetime


class Product:
    """Represents a single product in the supermarket"""
    
    def __init__(self, product_id: str, name: str, category: str, 
                 price: float, quantity: int, added_date: str = None):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.added_date = added_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def display(self):
        """Display product details in formatted way"""
        print("\n" + "="*50)
        print(f"Product ID      : {self.product_id}")
        print(f"Product Name    : {self.name}")
        print(f"Category        : {self.category}")
        print(f"Price           : ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")
        print(f"Added Date      : {self.added_date}")
        print("="*50)
    
    def display_compact(self):
        """Display product in compact format (for lists)"""
        print(f"[{self.product_id}] {self.name} - ${self.price:.2f} (Stock: {self.quantity})")
    
    def is_out_of_stock(self) -> bool:
        """Check if product is out of stock"""
        return self.quantity <= 0
    
    def to_list(self) -> list:
        """Convert to list for CSV storage"""
        return [self.product_id, self.name, self.category, 
                f"{self.price:.2f}", str(self.quantity), self.added_date]
    
    @staticmethod
    def from_list(data: list) -> 'Product':
        """Create Product object from CSV row"""
        product_id, name, category = data[0], data[1], data[2]
        price = float(data[3])
        quantity = int(data[4])
        added_date = data[5] if len(data) > 5 else None
        return Product(product_id, name, category, price, quantity, added_date)


class CartItem:
    """Represents an item in the shopping cart"""
    
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
    
    def get_total(self) -> float:
        """Calculate total price for this item"""
        return self.product.price * self.quantity
    
    def display(self):
        """Display cart item details"""
        print(f"{self.product.name:20} x {self.quantity:3} @ ${self.product.price:7.2f} = ${self.get_total():7.2f}")


class ShoppingCart:
    """Represents a customer's shopping cart"""
    
    def __init__(self):
        self.items = {}  # Key: product_id, Value: CartItem
    
    def add_item(self, product: Product, quantity: int) -> bool:
        """Add item to cart"""
        if quantity <= 0:
            return False
        
        if product.product_id in self.items:
            self.items[product.product_id].quantity += quantity
        else:
            self.items[product.product_id] = CartItem(product, quantity)
        return True
    
    def remove_item(self, product_id: str) -> bool:
        """Remove item from cart"""
        if product_id in self.items:
            del self.items[product_id]
            return True
        return False
    
    def get_total(self) -> float:
        """Calculate total cart price"""
        return sum(item.get_total() for item in self.items.values())
    
    def get_item_count(self) -> int:
        """Get number of items in cart"""
        return len(self.items)
    
    def is_empty(self) -> bool:
        """Check if cart is empty"""
        return len(self.items) == 0
    
    def clear(self):
        """Clear all items from cart"""
        self.items.clear()
    
    def display(self):
        """Display cart contents"""
        if self.is_empty():
            print("\nCart is empty!")
            return
        
        print("\n" + "="*60)
        print("SHOPPING CART")
        print("="*60)
        print(f"{'Product Name':<20} {'Qty':>3} {'Price':>10} {'Total':>10}")
        print("-"*60)
        
        for item in self.items.values():
            item.display()
        
        print("-"*60)
        print(f"{'TOTAL':<20} {'':<3} {'':<10} ${self.get_total():>8.2f}")
        print("="*60)