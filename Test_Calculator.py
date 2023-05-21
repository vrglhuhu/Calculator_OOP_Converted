# Vergel, Chean Bernard Villanueva
# Calculator_OOP_Converted

from user_interface import User_interface
from Calculator_OOP_Converted import Calculator
from greetings import Greeting

greeting = Greeting()
calculator = Calculator()
ui = User_interface()
greeting.print_welcome_message()

while True:
    choice = ui.get_user_choice()
    if choice in calculator.operations:
        if choice.upper() == "A":
           calculator.addition()
        elif choice.upper() == "B":
           calculator.subtraction()  
        elif choice.upper() == "C":
           calculator.multiplication()
        else:
           calculator.division() 
        if not ui.continue_calculation():
            print("\033[32mI hope this program helps and satisfy you.\033[0m")
            break
    else:
        print("\U0001F6A7 \033[31mINVALID INPUT!\033[0m\U0001F6A7")

greeting.print_goodbye_message()