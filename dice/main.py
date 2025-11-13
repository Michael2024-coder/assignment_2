import sys
from pathlib import Path

from dice.game import Game


class Main:
    def __init__(self):
        self.game = Game()
    
    def menu(self) -> str:
        print("\n------ Main Menu ------")
        print("1. Play Game\n2. Highscore\n3. Quit")
        return input("Select an option (1/2/3): ")
    
    def display_rules(self) -> None:
        print("\n---------- Welcome to Two-Dice Pig! ----------\n")
        strs = "Game Rules"
        print("\n------------------------------------------")
        print(f"| {strs:^38s}")
        print("------------------------------------------")
        with open('dice/rules.txt', 'r') as game_rules:
            print(f"{game_rules.read().strip()}")
            
        game_rules.close()
        print("------------------------------------------")
        
    def play(self) -> None:
        self.display_rules()
        input("Press Enter to continue...")
        while True:
            option = self.menu()
            match(option):
                case "1":
                    self.game.start_game()
                case "2":
                    pass
                case "3":
                    break
                case _:
                    print("Wrong Input! Enter Valid Option.")
        
if __name__ == "__main__":
    # Allow running directly from VS Code or terminal
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    MAIN = Main()
    MAIN.play()