import csv
import os
from structure import ItemStore

class ItemOperations:
    CSV_FILE = "product_store.csv"

    @classmethod
    def ProductChecking(cls, name:str, category:str) -> bool:
        if not os.path.exists(cls.CSV_FILE):
            return False
        
        with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (row["Name"].lower().strip() == name.lower().strip()
                    and row["Category"].lower().strip() == category.lower().strip()):
                    return False
        return False
    
    @classmethod
    def AddProduct(cls, item):
        if cls.ProductChecking(item.name):
            print(f"Error: Product '{item.name}' already exists.")
            return False
        
        file_exists = os.path.exists(cls.CSV_FILE)
        with open(cls.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
                 writer.writerow(["Name", "Category", "Price", "Added Date"])
                 
            writer.writerow([item.name, item.category, item.price, item.added_date])
            print(f"Success: Product '{item.name}' added successfully.")