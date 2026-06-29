from typing import Optional
from model import Place
from Repository import PlaceRepository


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