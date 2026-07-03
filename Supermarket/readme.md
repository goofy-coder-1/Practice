# Supermarket Management System - Complete Project

## Project Overview

A complete supermarket inventory and shopping cart management system built with Python using OOP principles and modular architecture.

## Project Structure

```
supermarket_project/
├── supermarket_main.py          # Entry point - run this file
├── supermarket_app.py           # Presentation layer (UI/Menu)
├── supermarket_service.py       # Business logic layer
├── supermarket_repository.py    # Data access layer (CSV operations)
├── supermarket_models.py        # Data models (Product, Cart, etc.)
├── inventory.csv                # Data file (auto-created)
└── README.md                    # This file
```

## Features

### 1. Inventory Management
- ✓ Add new products
- ✓ View all products (formatted table)
- ✓ View product details
- ✓ Update product information (name, price, quantity)
- ✓ Delete products
- ✓ Search products by name (partial match)
- ✓ Filter products by category
- ✓ View low stock alerts

### 2. Shopping Cart
- ✓ Add products to cart
- ✓ Remove products from cart
- ✓ View cart with calculated totals
- ✓ Clear entire cart
- ✓ Checkout with automatic inventory update
- ✓ Cart total calculation

### 3. Data Management
- ✓ Persistent CSV storage
- ✓ Automatic inventory updates after checkout
- ✓ Product ID uniqueness validation
- ✓ Quantity tracking

## File Descriptions

### supermarket_main.py (Entry Point)
```python
from supermarket_app import SupermarketApp

if __name__ == "__main__":
    app = SupermarketApp()
    app.run()
```
- Simple entry point
- Always run this file to start the application

### supermarket_models.py (Data Models)
Defines three classes:

#### 1. Product
Represents a product in the supermarket
```python
Product(product_id, name, category, price, quantity, added_date)
```

**Methods:**
- `display()` - Show full product details
- `display_compact()` - Show brief product info
- `is_out_of_stock()` - Check stock status
- `to_list()` - Convert to CSV format
- `from_list()` - Create from CSV row

**Attributes:**
- `product_id` - Unique identifier (e.g., "P001")
- `name` - Product name (e.g., "Apple")
- `category` - Category (e.g., "Fruits")
- `price` - Price per unit
- `quantity` - Stock quantity
- `added_date` - When product was added

#### 2. CartItem
Represents an item in the shopping cart
```python
CartItem(product, quantity)
```

**Methods:**
- `get_total()` - Calculate total price for this item
- `display()` - Show formatted cart item

#### 3. ShoppingCart
Represents a customer's shopping cart
```python
ShoppingCart()
```

**Methods:**
- `add_item(product, quantity)` - Add item to cart
- `remove_item(product_id)` - Remove item from cart
- `get_total()` - Get total cart price
- `get_item_count()` - Get number of unique items
- `is_empty()` - Check if cart is empty
- `clear()` - Clear all items
- `display()` - Show formatted cart

### supermarket_repository.py (Data Access)
Handles all CSV file operations

**Methods:**
```python
save(product)                    # Add new product
get_by_id(product_id)           # Find product by ID
get_all()                       # Get all products
get_by_category(category)       # Find products in category
update(product_id, product)     # Update product
delete(product_id)              # Delete product
search_by_name(name)            # Search by name (partial match)
get_low_stock(threshold)        # Get products with low inventory
```

**Features:**
- Automatic file creation with headers
- Duplicate product ID prevention
- Error handling for file operations
- Type conversion (string ↔ Product)

### supermarket_service.py (Business Logic)
Core application logic

**Product Management:**
- `add_product()` - Add with validation
- `view_all_products()` - Display formatted table
- `view_product()` - Show details
- `update_product()` - Edit existing product
- `delete_product()` - Remove product
- `search_products()` - Find by name
- `view_by_category()` - Filter by category
- `view_low_stock()` - Inventory alerts

**Shopping Cart:**
- `add_to_cart()` - Add with stock check
- `view_cart()` - Display cart contents
- `remove_from_cart()` - Remove item
- `clear_cart()` - Empty cart
- `checkout()` - Process sale & update inventory

**Validation:**
- `validate_product_input()` - Check product data

### supermarket_app.py (Presentation)
User interface and menu system

**Methods:**
- `display_main_menu()` - Show options
- `handle_inventory_menu()` - Route inventory operations
- `handle_cart_menu()` - Route cart operations
- `run()` - Main application loop

## How to Run

### Step 1: Organize Files
Place all 5 Python files in the same directory:
```
your_project_folder/
├── supermarket_main.py
├── supermarket_app.py
├── supermarket_service.py
├── supermarket_repository.py
└── supermarket_models.py
```

### Step 2: Start Application
```bash
python supermarket_main.py
```

### Step 3: Use the Menu
```
==================================================
SUPERMARKET MANAGEMENT SYSTEM
==================================================

1. INVENTORY MANAGEMENT
   1.1 - Add Product
   1.2 - View All Products
   1.3 - View Product Details
   1.4 - Update Product
   1.5 - Delete Product
   1.6 - Search Products
   1.7 - View by Category
   1.8 - View Low Stock Items

2. SHOPPING CART
   2.1 - Add to Cart
   2.2 - View Cart
   2.3 - Remove from Cart
   2.4 - Clear Cart
   2.5 - Checkout

3. Exit
==================================================
```

## Usage Examples

### Example 1: Add a Product
```
Choose: 1.1
Enter product ID: P001
Enter product name: Apples
Enter category: Fruits
Enter price: 2.99
Enter quantity: 50

Product will be displayed for confirmation
```

### Example 2: Add to Cart and Checkout
```
Choose: 2.1
Enter product ID: P001
Enter quantity: 3

Choose: 2.2 (View cart to verify)

Choose: 2.5 (Checkout)
Inventory automatically updated!
```

### Example 3: Search Products
```
Choose: 1.6
Enter product name: Apple
Found products matching "Apple"
```

## CSV File Format

**inventory.csv**
```csv
Product ID,Name,Category,Price,Quantity,Added Date
P001,Apples,Fruits,2.99,47,2024-01-15 10:30:00
P002,Milk,Dairy,3.50,25,2024-01-15 11:00:00
P003,Bread,Bakery,2.50,18,2024-01-15 11:15:00
```

After adding to cart and checking out:
- Quantities are automatically updated
- New products can be added anytime
- Historical data is preserved

## Architecture Pattern

### Dependency Chain
```
supermarket_main.py
        ↓
supermarket_app.py
        ↓
supermarket_service.py
        ↓
supermarket_repository.py
        ↓
supermarket_models.py
```

Each layer only depends on layers below it.

### Separation of Concerns
- **Models**: Pure data (no logic)
- **Repository**: Storage only (no business logic)
- **Service**: Business logic (no UI, no storage details)
- **App**: UI only (no business logic)
- **Main**: Just runs the app

## Key OOP Principles Used

### 1. Single Responsibility
- Each class has ONE job
- `Product` - just data
- `ProductRepository` - just CSV operations
- `SupermarketService` - just business logic
- `SupermarketApp` - just UI

### 2. Encapsulation
- Cart items stored in dictionary (internal detail)
- `display()` methods hide formatting
- `to_list()` and `from_list()` hide CSV structure

### 3. Data Validation
- Input validation in service layer
- Price and quantity checks
- Product ID uniqueness checks
- Stock availability checks

### 4. Error Handling
- Try/except blocks for file operations
- User-friendly error messages
- Graceful failure handling

### 5. Type Hints
```python
def add_to_cart(self, product: Product, quantity: int) -> bool:
    # Clear types for all parameters and return
```

## Advanced Features

### 1. Low Stock Alerts
Identify products that need reordering:
```python
products = repository.get_low_stock(threshold=5)
```

### 2. Category Filtering
Group products by type:
```python
fruits = repository.get_by_category("Fruits")
```

### 3. Search Functionality
Find products with partial name match:
```python
results = repository.search_by_name("app")  # Finds "Apple", "Pineapple"
```

### 4. Dynamic Inventory Updates
Automatically update stock after checkout:
```python
# Quantity reduced during checkout
# No manual inventory adjustment needed
```

### 5. Cart Calculations
Automatic total and subtotal calculations:
```python
cart.get_total()         # $XX.XX
cart.get_item_count()    # 3 items
```

## How to Extend

### Add Sales History
```python
class Sale:
    def __init__(self, product_id, quantity, total, date):
        self.product_id = product_id
        self.quantity = quantity
        self.total = total
        self.date = date

class SalesRepository:
    def save_sale(self, sale):
        # Save to CSV or database
```

### Add User Accounts
```python
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class CustomerRepository:
    def save(self, customer):
        # Save to CSV
```

### Switch to Database
```python
class DatabaseRepository:
    def __init__(self, connection_string):
        self.db = connect(connection_string)
    
    def save(self, product):
        query = "INSERT INTO products VALUES ..."
        self.db.execute(query)
```

### Add Discount System
```python
class Discount:
    def __init__(self, percentage, min_items):
        self.percentage = percentage
        self.min_items = min_items

# Apply in checkout:
if cart.get_item_count() >= discount.min_items:
    total *= (1 - discount.percentage/100)
```

## Troubleshooting

### ImportError: No module named 'supermarket_models'
- Make sure all files are in the same directory
- Check file names match exactly

### CSV file not created
- Files are created automatically on first use
- Ensure directory is writable
- Check file permissions

### Product ID already exists error
- Product IDs must be unique
- Use different ID for new products

### Out of stock error
- Product quantity is 0
- Update inventory before purchasing

## Testing

### Manual Testing Workflow
1. Add 3-4 products with different categories
2. Search for a product
3. View by category
4. Add multiple items to cart
5. Remove one item
6. Checkout
7. Verify inventory updated
8. Check low stock

### Test Cases
```python
def test_add_product():
    service = SupermarketService()
    product = Product("P001", "Test", "Test", 10.0, 5)
    assert service.repository.save(product)

def test_checkout():
    service = SupermarketService()
    product = Product("P001", "Apple", "Fruit", 2.99, 10)
    service.repository.save(product)
    service.cart.add_item(product, 3)
    assert service.cart.get_total() == 8.97
    assert service.cart.get_item_count() == 1
```

## Performance

| Operation | Time | Scalability |
|-----------|------|-------------|
| Add product | O(1) | Good |
| View all | O(n) | Good for <10k products |
| Search | O(n) | Good for <10k products |
| Update | O(n) | Good for <10k products |
| Delete | O(n) | Good for <10k products |
| Checkout | O(m) | m = cart items |

For larger datasets, consider using a database instead of CSV.

## Future Enhancements

- [ ] Database integration (SQLite, MySQL)
- [ ] User authentication
- [ ] Sales history and analytics
- [ ] Barcode scanner support
- [ ] Multi-store management
- [ ] Price history tracking
- [ ] Bulk order discounts
- [ ] Supplier management
- [ ] Web interface (Flask/Django)
- [ ] Mobile app (React Native)

## Project Statistics

| Metric | Count |
|--------|-------|
| Files | 5 |
| Total Lines | ~650 |
| Classes | 5 |
| Methods | 30+ |
| Features | 18 |

## Learning Outcomes

By completing this project, you've learned:
✓ Modular architecture (layered design)
✓ Object-oriented programming (classes, methods)
✓ Data persistence (CSV file handling)
✓ Error handling and validation
✓ Business logic separation
✓ User interface design
✓ Code organization and naming
✓ Type hints and documentation
✓ Encapsulation and abstraction
✓ Testing strategies

## Summary

This is a production-quality project that demonstrates:
- **Professional** OOP design patterns
- **Clean** code architecture
- **Scalable** modular structure
- **Maintainable** separation of concerns
- **Extensible** for new features

Great work on learning these concepts! 🚀