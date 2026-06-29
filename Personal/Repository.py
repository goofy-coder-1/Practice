import csv
import os
from typing import Optional, List
from model import Place


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