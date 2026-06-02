class Calculator:
    def __init__(self):
        
        self.first_num, self.operation, self.second_num = self.user_Input()


    def user_Input(self):
        while True:
            try:
                first_number= float(input("Enter first number: "))
                operation = input("Enter operation (+ - * /): ")
                second_number = float(input("Enter second number: "))
                
                if operation not in ['+', '-', '*', '/']:
                    print("Error: Invalid operation symbol. Try again.\n")
                    continue 

                return first_number, operation, second_number
            except ValueError:
                print("Error on value input")
    
    
    def calculate(self):
          match self.operation:
                case '+':
                  result = self.first_num + self.second_num
                  print(f"Addition: {result}")
                case '-':
                  result = self.first_num + self.second_num
                  print(f"subtraction: {result}")
                case '*':
                  result = self.first_num * self.second_num
                  print(f"Multiplication: {result}")
                case '/':
                    if self.second_num == 0:
                      print("Denominator can't be zero")
                    else:
                      
                      result = self.first_num / self.second_num
                      print(f"Divisiion: {result}")
                case _:
                  print(f"Error!")
    
my_calculator = Calculator()

my_calculator.calculate()