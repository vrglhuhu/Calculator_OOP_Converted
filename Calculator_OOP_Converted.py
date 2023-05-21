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
    def subtraction(self):
        print("\U0001F530 \033[40m\033[35mSUBTRACTION OPERATION\033[0m \U0001F530")
        try:
            num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to subtract:\033[0m "))
            num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to subtract:\033[0m "))
            subtract = num1 - num2
            print("\U0001F7E5 TOTAL \U0001F7E5")
            print(num1, "-", num2, "=", subtract)
        except ValueError:
            print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a number.\033[0m")

    # Perform subtraction operation and display the result
    def subtraction(self):
        print("\U0001F530 \033[40m\033[35mSUBTRACTION OPERATION\033[0m \U0001F530")
        try:
            num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to subtract:\033[0m "))
            num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to subtract:\033[0m "))
            subtract = num1 - num2
            print("\U0001F7E5 TOTAL \U0001F7E5")
            print(num1, "-", num2, "=", subtract)
        except ValueError:
            print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a number.\033[0m")

    # Perform multiplication operation and display the result
    def multiplication(self):
        print("\U0001F530 \033[40m\033[35mMULTIPLICATION OPERATION\033[0m \U0001F530")
        try:
            num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to multiply:\033[0m "))
            num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to multiply:\033[0m "))
            multiply = num1 * num2
            print("\U0001F7E5 TOTAL \U0001F7E5")
            print(num1, "*", num2, "=", multiply)
        except ValueError:
            print("\U0001F6A7 \033[31mINVALID INPUT. Please enter a number.\033[0m")
    # Perform division operation and display the result
    def division(self):
        print("\U0001F530 \033[40m\033[35mDIVISION OPERATION\033[0m \U0001F530")
        try:
            num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to divide:\033[0m "))
            num2 = float(input("\U0001F4E2 \033[40m\033[34mEnter second number that you want to divide:\033[0m "))
            divide = num1 / num2
            print("\U0001F7E5 TOTAL \U0001F7E5")
            print(num1, "/", num2, "=", divide)
        except (ValueError, ZeroDivisionError):
            print("\U0001F6A7 \033[31mINVALID INPUT. Please enter an integer or a non-zero number.\033[0m")

    # Ask the user if they want to perform another calculation
    # Print closing message
