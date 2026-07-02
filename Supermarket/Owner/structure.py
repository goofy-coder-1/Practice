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