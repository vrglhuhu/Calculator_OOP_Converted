# Vergel, Chean Bernard Villanueva
# Calculator_OOP_Converted

import pyfiglet

# Make class for calculator
class Calculator:
    # Initialize operations dictionary with operation names as keys and corresponding methods as values 
    def __init__(self):
        self.operations = {
            "a": self.addition,
            "b": self.subtraction,
            "c": self.multiplication,
            "d": self.division
        }
    # Make a def for the welcome message
    def print_welcome_message(self):
        print("=" * 110)
        print("=" * 110)
        welcome = pyfiglet.figlet_format("Simple App Calculator".center(55), font="digital")
        print(welcome)
        print("=" * 110)
        print("=" * 110)
        print("\n\033[40m\033[33mTo select an operation.\033[0m")
        print("\U0001F6D1 \033[31mPress A: \033[0m Addition")
        print("\U0001F6D1 \033[32mPress B: \033[0m Subtraction")
        print("\U0001F6D1 \033[33mPress C: \033[0m Multiplication")
        print("\U0001F6D1 \033[34mPress D: \033[0m Division\n")

    # Get user's choice of operation
    def get_user_choice(self):
        choice = input("\033[40m\033[33mEnter your choice of operation:\033[0m ")
        return choice.upper()
    
    # Perform addition operation and display the result
    # Perform subtraction operation and display the result
    # Perform multiplication operation and display the result
    # Perform division operation and display the result
    # Ask the user if they want to perform another calculation
    # Print closing message
