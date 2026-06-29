import csv
import os
from datetime import datetime
from typing import Optional, List


# ============= MODEL LAYER =============
class Place:
    """Represents a single place in the bucket list"""
    
    def __init__(self, name: str, address: str, reason: str, 
                 added_date: str = None):
        self.name = name
        self.address = address
        self.reason = reason
        self.added_date = added_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def display(self):
        """Display place details in formatted way"""
        print("\n" + "="*40)
        print(f"Place Name      : {self.name}")
        print(f"Address         : {self.address}")
        print(f"Reason to Visit : {self.reason}")
        print(f"Added Date      : {self.added_date}")
        print("="*40)
    
    def to_list(self) -> list:
        """Convert to list for CSV storage"""
        return [self.name, self.address, self.reason, self.added_date]
    
    @staticmethod
    def from_list(data: list) -> 'Place':
        """Create Place object from CSV row"""
        name, address, reason = data[0], data[1], data[2]
        added_date = data[3] if len(data) > 3 else None
        return Place(name, address, reason, added_date)


# ============= DATA ACCESS LAYER =============
class PlaceRepository:
    """Handles all file I/O operations for places"""
    
    CSV_FILE = "bucketlist.csv"
    HEADERS = ["Name", "Address", "Reason", "Added Date"]
    
    @classmethod
    def _ensure_file_exists(cls):
        """Create CSV file with headers if it doesn't exist"""
        if not os.path.exists(cls.CSV_FILE):
            with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(cls.HEADERS)
    
    @classmethod
    def save(cls, place: Place) -> bool:
        """Save a new place to CSV"""
        try:
            cls._ensure_file_exists()
            
            with open(cls.CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(place.to_list())
            return True
        except IOError as e:
            print(f"Error saving place: {e}")
            return False
    
    @classmethod
    def get_by_name(cls, name: str) -> Optional[Place]:
        """Retrieve a place by name"""
        try:
            if not os.path.exists(cls.CSV_FILE):
                return None
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[0].strip().lower() == name.strip().lower():
                        return Place.from_list(row)
            return None
        except IOError as e:
            print(f"Error retrieving place: {e}")
            return None
    
    @classmethod
    def get_all(cls) -> List[Place]:
        """Retrieve all places"""
        places = []
        try:
            if not os.path.exists(cls.CSV_FILE):
                return places
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row:
                        places.append(Place.from_list(row))
            return places
        except IOError as e:
            print(f"Error retrieving places: {e}")
            return places
    
    @classmethod
    def update(cls, old_name: str, place: Place) -> bool:
        """Update an existing place"""
        try:
            if not os.path.exists(cls.CSV_FILE):
                return False
            
            places = []
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[0].strip().lower() == old_name.strip().lower():
                        places.append(place.to_list())
                    else:
                        places.append(row)
            
            # Write back all places
            with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(cls.HEADERS)
                writer.writerows(places)
            return True
        except IOError as e:
            print(f"Error updating place: {e}")
            return False
    
    @classmethod
    def delete(cls, name: str) -> bool:
        """Delete a place by name"""
        try:
            if not os.path.exists(cls.CSV_FILE):
                return False
            
            places = []
            found = False
            
            with open(cls.CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                
                for row in reader:
                    if row and row[0].strip().lower() == name.strip().lower():
                        found = True
                    else:
                        places.append(row)
            
            if not found:
                return False
            
            # Write back remaining places
            with open(cls.CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(cls.HEADERS)
                writer.writerows(places)
            return True
        except IOError as e:
            print(f"Error deleting place: {e}")
            return False


# ============= BUSINESS LOGIC LAYER =============
class BucketListService:
    """Handles business logic and user interactions"""
    
    def __init__(self):
        self.repository = PlaceRepository()
    
    @staticmethod
    def validate_input(name: str, address: str, reason: str) -> bool:
        """Validate user input"""
        if not name.strip() or not address.strip() or not reason.strip():
            print("Error: All fields must be filled!")
            return False
        return True
    
    def add_place(self) -> Optional[Place]:
        """Add a new place to bucket list"""
        try:
            print("\n" + "="*40)
            print("ADD NEW PLACE")
            print("="*40)
            
            name = input("Enter name of place: ").strip()
            address = input("Enter address of place: ").strip()
            reason = input("Reason to visit the place: ").strip()
            
            if not self.validate_input(name, address, reason):
                return None
            
            # Check if place already exists
            if self.repository.get_by_name(name):
                print(f"Error: Place '{name}' already exists!")
                return None
            
            place = Place(name, address, reason)
            place.display()
            
            confirmation = input("\nSave this place? (yes/no): ").strip().lower()
            
            if confirmation in ["yes", "y"]:
                if self.repository.save(place):
                    print("✓ Place successfully added!")
                    return place
                else:
                    print("✗ Failed to save place.")
                    return None
            else:
                print("Operation cancelled.")
                return None
        except Exception as e:
            print(f"Error adding place: {e}")
            return None
    
    def view_place(self):
        """View details of a specific place"""
        print("\n" + "="*40)
        print("VIEW PLACE DETAILS")
        print("="*40)
        
        name = input("Enter place name to view: ").strip()
        
        if not name:
            print("Error: Place name cannot be empty!")
            return
        
        place = self.repository.get_by_name(name)
        
        if place:
            place.display()
        else:
            print(f"✗ Place '{name}' not found.")
    
    def view_all_places(self):
        """View all places in bucket list"""
        places = self.repository.get_all()
        
        if not places:
            print("\n✗ No places in bucket list yet!")
            return
        
        print("\n" + "="*40)
        print(f"BUCKET LIST ({len(places)} places)")
        print("="*40)
        
        for i, place in enumerate(places, 1):
            print(f"\n{i}. {place.name}")
            print(f"   Address: {place.address}")
            print(f"   Reason: {place.reason}")
            print(f"   Added: {place.added_date}")
    
    def update_place(self):
        """Update an existing place"""
        print("\n" + "="*40)
        print("UPDATE PLACE")
        print("="*40)
        
        old_name = input("Enter place name to update: ").strip()
        
        if not old_name:
            print("Error: Place name cannot be empty!")
            return
        
        place = self.repository.get_by_name(old_name)
        
        if not place:
            print(f"✗ Place '{old_name}' not found.")
            return
        
        print("\nCurrent details:")
        place.display()
        
        print("\nEnter new details (or press Enter to keep current):")
        name = input("New name: ").strip() or place.name
        address = input("New address: ").strip() or place.address
        reason = input("New reason: ").strip() or place.reason
        
        if not self.validate_input(name, address, reason):
            return
        
        updated_place = Place(name, address, reason, place.added_date)
        updated_place.display()
        
        confirmation = input("\nSave changes? (yes/no): ").strip().lower()
        
        if confirmation in ["yes", "y"]:
            if self.repository.update(old_name, updated_place):
                print("✓ Place successfully updated!")
            else:
                print("✗ Failed to update place.")
        else:
            print("Operation cancelled.")
    
    def delete_place(self):
        """Delete a place from bucket list"""
        print("\n" + "="*40)
        print("DELETE PLACE")
        print("="*40)
        
        name = input("Enter place name to delete: ").strip()
        
        if not name:
            print("Error: Place name cannot be empty!")
            return
        
        place = self.repository.get_by_name(name)
        
        if not place:
            print(f"✗ Place '{name}' not found.")
            return
        
        place.display()
        
        confirmation = input("\nAre you sure you want to delete this place? (yes/no): ").strip().lower()
        
        if confirmation in ["yes", "y"]:
            if self.repository.delete(name):
                print("✓ Place successfully deleted!")
            else:
                print("✗ Failed to delete place.")
        else:
            print("Operation cancelled.")


# ============= PRESENTATION LAYER =============
class BucketListApp:
    """Main application controller"""
    
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
        """Run the application"""
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


if __name__ == "__main__":
    app = BucketListApp()
    app.run()