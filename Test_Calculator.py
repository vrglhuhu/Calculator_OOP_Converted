# Vergel, Chean Bernard Villanueva
# Calculator_OOP_Converted

from Calculator_OOP_Converted import Calculator
from greetings import greeting

greeting = greeting()
calculator = Calculator()

greeting.print_welcome_message()
while True:
    choice = calculator.get_user_choice()
    if choice in calculator.operations:
        if choice.upper() == "A":
           calculator.addition()
        elif choice.upper() == "B":
           calculator.subtraction()  
        elif choice.upper() == "C":
           calculator.multiplication()
        elif calculator.division() == "D":
           calculator.division()  
        else:
            calculator.continue_calculation
            if calculator.continue_calculation.upper() == "YES":
                calculator.continue_calculation          
            else:
                if not calculator.continue_calculation():
                  break
    else:
        print("\U0001F6A7 \033[31mINVALID INPUT!\033[0m")
greeting.print_goodbye_message()