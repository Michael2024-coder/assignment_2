"""
Main module for running the Two-Dice Pig game application.

This module provides the `Main` class which serves as the central
controller for the application. It handles:

- Displaying the main menu
- Showing game rules
- Displaying player statistics
- Initializing and managing core game components (`Game` and `Histogram`)
- Running the main program loop

The module can be executed directly to start the game.
"""

import sys
from pathlib import Path
from dice.game import Game
from dice.histogram import Histogram


class Main:
    """
    Main application controller for the Two-Dice Pig game.

    Handles the game menu, displays rules, shows player statistics,
    and initializes core game components.
    """

    def __init__(self):
        """
        Initialize the Main controller with game and histogram managers.
        """
        self.game = Game()
        self.histogram = Histogram()

    def menu(self) -> str:
        """
        Display the main menu and prompt the user for an option.

        Returns:
            str: The user-selected menu option.
        """
        print("\n------ Main Menu ------")
        print("1. Play Game\n2. Player Stats\n3. Quit")
        return input("Select an option (1/2/3): ")

    def display_rules(self) -> None:
        """
        Display the game rules by reading them from the rules file.
        """
        print("\n---------- Welcome to Two-Dice Pig! ----------\n")
        strs = "Game Rules"
        print("\n------------------------------------------")
        print(f"| {strs:^38s}")
        print("------------------------------------------")
        with open('dice\\rules.txt', 'r', encoding='utf-8') as game_rules:
            print(f"{game_rules.read().strip()}")
        print("------------------------------------------")

    def display_stats(self) -> None:
        """
        Display stored player statistics such as high scores,
        games played, wins, and losses.
        """
        stats_dict = self.histogram.load_stats_file()
        for key in stats_dict.values():
            lst = list(key.values())
            print(f"\nUsername: {lst[0]}")
            print(f"Highscore: {lst[1]}")
            print(f"Games Played: {lst[2]}")
            print(f"Games Won: {lst[3]}")
            print(f"Games Lost: {lst[4]}")

    def play(self) -> None:
        """
        Run the main program loop:
        - Show rules
        - Display menu
        - Start game or show stats based on user input
        """
        self.display_rules()
        input("Press Enter to continue...")
        while True:
            option = self.menu()
            match(option):
                case "1":
                    self.game.start_game()
                case "2":
                    print("\n------- Player Statistics -------")
                    self.display_stats()
                case "3":
                    break
                case _:
                    print("Wrong Input! Enter Valid Option.")


if __name__ == "__main__":
    # Allow running directly from VS Code or terminal
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    MAIN = Main()
    MAIN.play()
