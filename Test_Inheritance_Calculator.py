# Vergel, Chean Bernard Villanueva
# Inheritance Calculator

from Inheritance_UserInterface import InheritUserInterface
from Inheritance_calculator import InheritCalculator
from Inheritance_greeting import InheritGreeting

greeting = InheritGreeting()
calculator = InheritCalculator()
ui = InheritUserInterface()
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
        elif choice.upper() == "D":
           calculator.division()
        else:
           calculator.factorial() 
        if not ui.continue_calculation():
            print("\033[32mI hope this program helps and satisfy you.\033[0m")
            break
    else:
        print("\U0001F6A7 \033[31mINVALID INPUT!\033[0m\U0001F6A7")

greeting.print_goodbye_message()