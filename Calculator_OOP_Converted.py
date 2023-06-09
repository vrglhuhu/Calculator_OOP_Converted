# Vergel, Chean Bernard Villanueva
# Calculator_OOP_Converted

# Make class for calculator
class Calculator:
    # Initialize operations dictionary with operation names as keys and corresponding methods as values 
    def __init__(self):
        self.operations = {
            "A": self.addition,
            "B": self.subtraction,
            "C": self.multiplication,
            "D": self.division
        }
          
    # Perform addition operation and display the result
    def addition(self):
        print("\U0001F530 \033[40m\033[35mADDITION OPERATION\033[0m \U0001F530")
        try:
            num1 = float(input("\U0001F4E2 \033[40m\033[34mEnter first number that you want to add:\033[0m "))
            num2 = float(input("\U0001F4E2  \033[40m\033[34mEnter second number that you want to add:\033[0m "))
            add = num1 + num2
            print("\U0001F7E5 TOTAL \U0001F7E5")
            print(num1, "+", num2, "=", add)
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
