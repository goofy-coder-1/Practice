from datetime import datetime

class ItemStructure:
    def __init__(self, name:str, category:str, price:int, added_date:str = None):
           self.name = name
           self.category = category
           self.price = price
           self.added_date = added_date or datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    def DisplayDetails(self):
          print("\n"+"="*40)
          print("="*13+"Details Below"+"="*14)
          print(f"Name         :   {self.name}")
          print(f"Category     :   {self.category}")
          print(f"Price        :   {self.price}")
          print(f"Added Date   :   {self.added_date}")
