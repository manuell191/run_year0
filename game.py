class Game:
    def __init__(self):
        self.running = True

    def introduction(self):
        # function to keep introduction organized
        pass

    def process_input(self, user_in):
        if user_in == "exit":
            self.running = False

    def run(self):
        # temporary introduction
        print("Welcome to the world of Run!")
        
        # regular game loop
        while self.running:
            print("What do you want to do?")
            user_in = input(": ")
            process_input(user_in)

        # if game ends
        print("Thanks for playing!")
