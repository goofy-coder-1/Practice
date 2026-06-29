
# Bucket List Application - Modular Version

## Project Structure

```
bucket_list_project/
├── main.py              # Entry point - run this file
├── app.py               # Presentation layer (UI/Menu)
├── service.py           # Business logic layer
├── repository.py        # Data access layer (CSV operations)
├── models.py            # Data model (Place class)
├── bucketlist.csv       # Data file (created when you add places)
└── README.md            # This file
```

## File Descriptions

### 1. **main.py** (Entry Point)
- Minimal file - just imports and runs the app
- Execute this file to start the application
- Keeps clean separation between code and execution

```bash
python main.py
```

### 2. **app.py** (Presentation Layer)
- Displays menu to user
- Handles user input for menu navigation
- Calls appropriate service methods
- **No business logic here** - just UI

### 3. **service.py** (Business Logic Layer)
- All application rules and logic
- Validates user input
- Checks for duplicates
- Calls repository methods
- **No file I/O here** - uses repository

### 4. **repository.py** (Data Access Layer)
- All CSV file operations
- CRUD (Create, Read, Update, Delete)
- Handles file errors
- **No business logic here** - just data operations

### 5. **models.py** (Data Model)
- Defines `Place` class
- Data representation
- Has methods like `to_list()` and `from_list()`
- **No dependencies** on other files (except datetime)

### 6. **bucketlist.csv** (Data File)
- Auto-created when you add first place
- Stores all your places
- CSV format: Name, Address, Reason, Added Date

---

## How to Run

### Step 1: Place all files in same directory
```
your_project_folder/
├── main.py
├── app.py
├── service.py
├── repository.py
└── models.py
```

### Step 2: Run the application
```bash
python main.py
```

### Step 3: Use the menu
```
========================================
BUCKET LIST APPLICATION
========================================
1. Add a new place
2. View all places
3. View place details
4. Update a place
5. Delete a place
6. Exit
========================================
```

---

## Dependency Chain

Each file only imports from files "below" it:

```
main.py
  ↓
app.py
  ↓
service.py
  ↓
repository.py
  ↓
models.py
```

This is called **clean architecture** or **layered architecture**.

**Benefits:**
- Each layer can be tested independently
- Easy to swap implementations (e.g., CSV → Database)
- Code is reusable
- Changes in one layer don't break others

---

## Example: How Imports Work

```python
# main.py imports only app
from app import BucketListApp

# app.py imports only service
from service import BucketListService

# service.py imports repository and models
from repository import PlaceRepository
from models import Place

# repository.py imports models
from models import Place

# models.py has no project dependencies
from datetime import datetime
```

---

## How to Extend the Project

### Add JSON storage instead of CSV?
```python
# Create repository_json.py
class JsonPlaceRepository:
    # Implement save(), get_all(), etc. with JSON
    
# Update service.py
def __init__(self):
    self.repository = JsonPlaceRepository()  # Swap implementation!
```

### Add search functionality?
```python
# Add to repository.py
@classmethod
def search_by_address(cls, address: str) -> List[Place]:
    # Search implementation

# Add to service.py
def search_places(self):
    address = input("Enter address: ")
    places = self.repository.search_by_address(address)
    # Display results

# Add menu option in app.py
elif choice == "7":
    self.service.search_places()
```

### Add database?
```python
# Create repository_db.py
class DatabasePlaceRepository:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def save(self, place: Place) -> bool:
        # Database insert
        
    # Implement other methods...

# Update service.py to use it
```

**No changes needed to app.py or models.py!** That's the power of layered architecture.

---

## File Sizes

| File | Lines | Purpose |
|------|-------|---------|
| main.py | ~5 | Entry point |
| app.py | ~40 | User interface |
| service.py | ~130 | Business logic |
| repository.py | ~120 | Data access |
| models.py | ~35 | Data model |
| **Total** | **~330** | Modular & clean |

Much easier to navigate than 330 lines in one file!

---

## Testing Example

With this structure, testing is easy:

```python
# test_service.py
from models import Place
from service import BucketListService

class MockRepository:
    def __init__(self):
        self.places = {}
    
    def save(self, place):
        self.places[place.name] = place
        return True
    
    def get_by_name(self, name):
        return self.places.get(name)

def test_add_place():
    service = BucketListService()
    service.repository = MockRepository()  # Swap with fake
    
    # Test without touching CSV files!
    place = Place("Paris", "France", "See Eiffel Tower")
    service.repository.save(place)
    
    retrieved = service.repository.get_by_name("Paris")
    assert retrieved.name == "Paris"
    print("✓ Test passed!")
```

---

## File Format: bucketlist.csv

After adding a place, your CSV looks like:

```csv
Name,Address,Reason,Added Date
Paris,France,See the Eiffel Tower,2024-01-15 10:30:45
Tokyo,Japan,Experience Japanese culture,2024-01-16 14:22:30
London,UK,Visit Big Ben,2024-01-17 09:15:20
```

Each row is a place you've added.

---

## Pros & Cons

### Pros of Modular Structure
✓ Easy to find code (organized by concern)
✓ Easy to test (each layer independent)
✓ Easy to extend (add features without breaking existing code)
✓ Easy to maintain (changes are localized)
✓ Professional structure (industry standard)
✓ Reusable code (import service in other projects)

### Cons
✗ More files to manage (but worth it!)
✗ Slightly more complex imports (but clear chain)
✗ Overkill for very small projects (but good for learning!)

---

## Quick Tips

1. **Always run from main.py**
   ```bash
   python main.py  # ✓ Correct
   python app.py   # ✗ Avoid (import errors)
   ```

2. **Keep directory structure flat** (all files in same folder initially)

3. **Use meaningful names** (app.py vs ui.py - both okay, be consistent)

4. **Each file should be under 200 lines** (easier to read)

5. **Import only what you need**
   ```python
   from models import Place  # ✓ Specific
   import models            # ✗ Too broad
   ```

---

## Summary

You now have a **professional, modular Python project** with:
- ✓ Clean architecture (4-layer pattern)
- ✓ Separation of concerns
- ✓ Easy to test, extend, and maintain
- ✓ Industry-standard structure
- ✓ Reusable components

Great learning progress! 🚀