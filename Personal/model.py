from datetime import datetime

class Place:
    def __init__(self, name: str, address : str, reason: str, added_date: str = None):
        self.name = name
        self.address = address
        self.reason = reason
        self.added_date = added_date or datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    def display(self):
        print("\n"+"="*40)
        print(f"Place Name      : {self.name}")
        print(f"Address         : {self.address}")
        print(f"Reason to Visit : {self.reason}")
        print(f"Added Date      : {self.added_date}")
        print("\n"+"="*40)

    def to_list(self) -> list:
        return [self.name, self.address, self.reason, self.added_date]
    
    @staticmethod
    def from_list(data: list) -> 'Place':
        name, address, reason = data[0], data[1], data[2]
        added_date = data[3] if len(data) > 3 else None
        return Place(name, address, reason, added_date)
   
   # bholi