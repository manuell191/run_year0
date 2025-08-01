import os

def clear_screen():
    # Check OS
    if os.name == "nt": # if windows
        os.system("cls")
    else:
        os.system("clear")
