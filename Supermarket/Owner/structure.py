from datetime import datetime

class ItemStructure:
    def __init__(self, name, category, price, added_date):
           self.name = name
           self.category = category
           self.price = price
           self.added_date = datetime.now("%Y-%m-%d %H-%M-%S")

    def DisplayDetails(self):
          print("\n"+"="*40)
          print("="*20+"Details Below"+"="*20)
          print(f"Name         :   {self.name}")
          print(f"Category     :   {self.category}")
          print(f"Price        :   {self.price}")
          print(f"Added Date   :   {self.added_date}")


