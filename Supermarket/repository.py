import csv
import os
from typing import Optional, List
from structure import Product


class ProductRepository:
    """Handles all file I/O operations for products"""
    
    CSV_FILE = "inventory.csv"
    HEADERS = ["Product ID", "Name", "Category", "Price", "Quantity", "Added Date"]
    
    @classmethod
    def _ensure_file_exists(cls):
        """Create CSV file with headers if it doesn't exist"""
        if not os.path.exists(cls.CSV_FILE):
            with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(cls.HEADERS)
    
    @classmethod
    def save(cls, product: Product) -> bool:
        """Save a new product to CSV"""
        try:
            cls._ensure_file_exists()
            
            # Check if product_id already exists
            if cls.get_by_id(product.product_id):
                return False
            
            with open(cls.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(product.to_list())
            return True
        except IOError as e:
            print(f"Error saving product: {e}")
            return False
    
    @classmethod
    def get_by_id(cls, product_id: str) -> Optional[Product]:
        """Retrieve a product by ID"""
        try:
            if not os.path.exists(cls.CSV_FILE):
                return None
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[0].strip() == product_id.strip():
                        return Product.from_list(row)
            return None
        except IOError as e:
            print(f"Error retrieving product: {e}")
            return None
    
    @classmethod
    def get_all(cls) -> List[Product]:
        """Retrieve all products"""
        products = []
        try:
            if not os.path.exists(cls.CSV_FILE):
                return products
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row:
                        products.append(Product.from_list(row))
            return products
        except IOError as e:
            print(f"Error retrieving products: {e}")
            return products
    
    @classmethod
    def get_by_category(cls, category: str) -> List[Product]:
        """Retrieve all products in a category"""
        products = []
        try:
            if not os.path.exists(cls.CSV_FILE):
                return products
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[2].strip().lower() == category.strip().lower():
                        products.append(Product.from_list(row))
            return products
        except IOError as e:
            print(f"Error retrieving products: {e}")
            return products
    
    @classmethod
    def update(cls, product_id: str, product: Product) -> bool:
        """Update an existing product"""
        try:
            if not os.path.exists(cls.CSV_FILE):
                return False
            
            products = []
            found = False
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[0].strip() == product_id.strip():
                        products.append(product.to_list())
                        found = True
                    else:
                        products.append(row)
            
            if not found:
                return False
            
            # Write back all products
            with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(cls.HEADERS)
                writer.writerows(products)
            return True
        except IOError as e:
            print(f"Error updating product: {e}")
            return False
    
    @classmethod
    def delete(cls, product_id: str) -> bool:
        """Delete a product by ID"""
        try:
            if not os.path.exists(cls.CSV_FILE):
                return False
            
            products = []
            found = False
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[0].strip() == product_id.strip():
                        found = True
                    else:
                        products.append(row)
            
            if not found:
                return False
            
            # Write back remaining products
            with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(cls.HEADERS)
                writer.writerows(products)
            return True
        except IOError as e:
            print(f"Error deleting product: {e}")
            return False
    
    @classmethod
    def search_by_name(cls, name: str) -> List[Product]:
        """Search products by name (partial match)"""
        products = []
        try:
            if not os.path.exists(cls.CSV_FILE):
                return products
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and name.lower() in row[1].lower():
                        products.append(Product.from_list(row))
            return products
        except IOError as e:
            print(f"Error searching products: {e}")
            return products
    
    @classmethod
    def get_low_stock(cls, threshold: int = 5) -> List[Product]:
        """Get products with stock below threshold"""
        products = []
        try:
            if not os.path.exists(cls.CSV_FILE):
                return products
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row:
                        product = Product.from_list(row)
                        if product.quantity < threshold:
                            products.append(product)
            return products
        except IOError as e:
            print(f"Error retrieving low stock items: {e}")
            return products