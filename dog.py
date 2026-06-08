class Dog:
    
    def __init__(self):
        self.name = ""
        self.height = 0
        self.personality = ""
    
    def getData(self):
        while True:
            try:
                self.name = input("Enter your dog's name: ")
                self.height = int(input("Enter your dog's height in cm: "))
                self.personality = input("What's their personality: ")
                break 
            except ValueError:
                print("Oops, height must be a number! Try again.\n")
    
    def persona(self):
        print(f"{self.name} who is {self.height}cm tall and has a {self.personality} personality barked for me!")


dog = Dog()
dog.getData()
dog.persona()