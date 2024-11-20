import os
import time
import sys
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# ASCII Banner
banner = """
██████╗  ██████╗ ███████╗████████╗███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝████╗ ████║██╔══██╗████╗  ██║
██████╔╝██║   ██║███████╗   ██║   ██╔████╔██║███████║██╔██╗ ██║
██╔═══╝ ██║   ██║╚════██║   ██║   ██║╚██╔╝██║██╔══██║██║╚██╗██║
██║     ╚██████╔╝███████║   ██║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

# Function to clear the terminal screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Loading animation with color
def loading_animation():
    loading_text = Fore.YELLOW + "Loading"
    for _ in range(5):
        sys.stdout.write(f"\r{loading_text + '.' * (_ % 3 + 1)}")
        sys.stdout.flush()
        time.sleep(1)

# Intro function with colors
def intro():
    clear_screen()
    
    # Print Banner with color
    print(Fore.CYAN + banner)
    time.sleep(1)
    
    # Welcome message with colors
    print(Fore.GREEN + "\nWelcome to PostMan!")
    time.sleep(0.5)
    print(Fore.GREEN + "Creator: " + Fore.BLUE + "https://github.com/Dev-0618/\n")
    
    # Loading animation
    loading_animation()
    
    # Transitioning message with colors
    print(Fore.GREEN + "\nTransitioning to the main program...\n")
    time.sleep(1)
    
    # Start the main program
    start_main_program()

# Function to start main program (simulating the start of main.py)
def start_main_program():
    print(Fore.GREEN + "Now running the main program...\n")
    time.sleep(1)
    
    # Run the main program (adjust path if needed)
    os.system('python3 module/main.py')

if __name__ == "__main__":
    intro()

