# Vergel, Chean Bernard Villanueva
# Calculator_OOP_Converted

import pyfiglet
class Greeting:
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
    
    # Print closing message
    def print_goodbye_message(self):
        print("\n\U0001F504\U0001F504 Closing Program... \U0001F504\U0001F504 Thank you!\n")
        goodbye = pyfiglet.figlet_format("Visit me again", font="puffy")
        print(goodbye)
        print("")