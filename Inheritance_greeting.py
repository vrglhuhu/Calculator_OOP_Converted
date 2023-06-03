# Vergel, Chean Bernard Villanueva
# Inheritance Calculator

from greetings import Greeting

class InheritGreeting(Greeting):
    # Make a def for the welcome message
    def print_welcome_message(self):
        super().print_welcome_message()
        print("\U0001F6D1 \033[36mPress E: \033[0m Factorial\n")
    
    # Print closing message
    def print_goodbye_message(self):
        print("\n\U0001F504\U0001F504 Program is now closing... \U0001F504\U0001F504 Thank you!\n")


