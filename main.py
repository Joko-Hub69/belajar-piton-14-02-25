import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        pass
    
    def increment_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0    
    pass

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_choice(self, choices):
        while True:
            choice = input("Kamu pilih apa? (rock, paper, scissor)")
            if choice in choices:
                return choice
            
            print("Invalid choice")
    pass

class Computer(Player):
    def __init__(self, name = "Computer"):
        super().__init__(name)

    def make_choice(self, choices):
        return random.choice(choices)
    pass

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor"]
        self.rules = {
            "rock": "scissor",
            "scissor": "paper",
            "paper": "rock"
        }
        self.human_player = None
        self.computer_player = Computer()
        self.win_score = 3
        self.round = 1

    def display_welcome_message(self):
        print("""
              Ayo main Rock, Paper, Scissors Game! Menang 3 kali artinya kamu Jagoan!
        """)

    def create_human_player(self):
        player_name = input("Masukkan nama kamu")
        self.human_player = Human(player_name)

    def play_round(self):
        print(f"Round {self.round}")

        computer_choice = self.computer_player.make_choice(self.choices)
        human_choice = self.human_player.make_choice(self.choices)

        print(f"Computer choice : {computer_choice}")
        print(f"Human choice : {human_choice}")

        if self.rules[computer_choice] == human_choice:
            self.computer_player.increment_score()
            print("Computer menang")
        elif self.rules[human_choice] == computer_choice:
            self.human_player.increment_score()
            print("Human menang")
        else:
            print("Sama njir, Seri Cuk!!")
    
        print(f"Computer Score: {self.computer_player.score}")
        print(f"Human Score: {self.human_player.score}")

        self.round += 1

    def check_winner(self):
        if self.computer_player.score == self.win_score:
            print("Kasian, kamu kalah")
            return True
        elif self.human_player.score == self.win_score:
            print("Ciyee, kamu menang Jagoan!")
            return True
        else:
            return False

    def play_again(self):
        ans = input("Main lagi gak neh? (Y/N)")
        return ans == "Y" or ans == "y" == ""

    def reset_game(self):
        self.computer_player.reset_score()
        self.human_player.reset_score()
        self.round = 1
        pass

    def start_game(self):
        self.display_welcome_message()
        self.create_human_player()

        while True:
            self.play_round()
            if self.check_winner():
                if self.play_again():
                    self.reset_game()
                else:
                    print("Suwun ya, wes gelem main!")
                    return
            pass
        pass
    pass

game = Game()
game.start_game()