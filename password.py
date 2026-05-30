
def setting_password():
    while True:
        try:
            name = input("Name: ")
            pass_word = input("Password: ")
            
            return name, pass_word
        except ValueError:
            print("wrong input!")

username, password = setting_password()

def login():
    while True:
        try:
           name = input("Username: ")
           pass_word = input("Password: ")

           return name, pass_word
        except ValueError:
            print("Wrong Input")
    
username_try, password_try = login()

def password_comparison(reg_name, reg_pass, try_name, try_pass):
    if reg_name == try_name and reg_pass == try_pass:
        print("--------------------------------------------------------")
        print(f"------------- W E L C O M E {reg_name.upper()}-----------------")
        print("--------------------------------------------------------") 
    else:
        print('-------------- wrong credentials ------------')
        

password_comparison(username, password, username_try, password_try)