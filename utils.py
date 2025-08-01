import os

def clear_screen() -> None:
    # check OS
    if os.name == "nt": # if windows
        os.system("cls")
    else:
        os.system("clear")

def clean_input(user_in) -> str:
    # return an easier string to process
    return user_in.lower().strip()
