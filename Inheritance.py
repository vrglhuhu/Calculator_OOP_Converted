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

