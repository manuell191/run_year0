from utils import clean_input, clear_screen
from game_objects.player_character import PlayerCharacter

class Game:
    def __init__(self) -> None:
        self.running: bool = True
        self.player: PlayerCharacter

    def introduction(self) -> None:
        # function to keep introduction organized
        pass

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
