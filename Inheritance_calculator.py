# Vergel, Chean Bernard Villanueva
# Inheritance Calculator

from Calculator_OOP_Converted import Calculator

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