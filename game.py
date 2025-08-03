from utils import clean_input, clear_screen
from game_objects.player_character import PlayerCharacter

class Game:
    def __init__(self) -> None:
        self.running: bool = True
        self.player: PlayerCharacter

    def introduction(self) -> None:
        # function to keep introduction organized
        print("Welcom to the world of Run!")
        print("Pick your starting class:")
        print("1: Warrior\n2: Knight\n3: Thief\n")

        while True:
            user_in: str = input(": ")
            user_in = clean_input(user_in)

            if user_in == "1" or user_in == "warrior":
                self.player = PlayerCharacter(1)
                break
            elif user_in == "2" or user_int == "knight":
                self.player = PlayerCharacter(2)
                break
            elif user_in == "3" or user_in == "thief":
                self.player = PlayerCharacter(3)
                break
            else:
                print("Invalid class. Try again.")

        print("Your adventure now begins")

    def process_input(self, user_in: str) -> None:
        # clean input before processing
        user_in: str = clean_input(user_in)

        if user_in == "exit":
            self.running = False

    def run(self) -> None:
        # temporary introduction
        print("Welcome to the world of Run!")
        
        # regular game loop
        while self.running:
            print("What do you want to do?")
            user_in: str = input(": ")
            self.process_input(user_in)

        # if game ends
        print("Thanks for playing!")
