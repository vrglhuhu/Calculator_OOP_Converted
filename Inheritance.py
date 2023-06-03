# Vergel, Chean Bernard Villanueva
# Inheritance Calculator

from greetings import Greeting
from user_interface import User_interface
from Calculator_OOP_Converted import Calculator

class InheritUserInterface(User_interface):
    pass

class InheritGreeting(Greeting):
    # Make a def for the welcome message
    def print_welcome_message(self):
        super().print_welcome_message()
        print("\U0001F6D1 \033[36mPress E: \033[0m Factorial")
    
    # Print closing message
    def print_goodbye_message(self):
        print("\n\U0001F504\U0001F504 Program is now closing... \U0001F504\U0001F504 Thank you!\n")

# Add a new method for calculating factorial
class InheritCalculator(Calculator):
    def __init__(self):
        self.operations = {
            "A": self.addition,
            "B": self.subtraction,
            "C": self.multiplication,
            "D": self.division,
            "E": self.factorial
        }

    def factorial(self):
        print("\U0001F4C2 \033[40m\033[35mFACTORIAL OPERATION\033[0m \U0001F4C2")
        try:
            num = int(input("\U0001F4E2 \033[40m\033[34mEnter the number for factorial calculation:\033[0m "))
            if num < 0:
                print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a non-negative integer.\033[0m")
            else:
                result = 1
                for i in range(1, num + 1):
                    result *= i
                print("\U0001F7E5 RESULT \U0001F7E5")
                print(num, "! =", result)
        except ValueError:
            print("\U0001F6A7 \033[31mINVALID INPUT. Please enter an integer.\033[0m")
