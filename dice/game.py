# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements

"""Main game controller for the Two-Dice Pig game."""

from __future__ import annotations
import sys
from pathlib import Path
from dice.player import Player
from dice.intelligence import Intelligence
from dice.histogram import Histogram
from dice.highscore import HighScore
from dice.dice_hand import DiceHand
sys.path.append(str(Path(__file__).resolve().parent.parent))


class Game:
    """Main game controller for Two-Dice Pig."""

    def __init__(self) -> None:
        """Initialize the game with players, scoring system, and dice mechanics."""

        self.dice_hand = DiceHand()
        self.ai_lvl = Intelligence()
        self.player = Player()
        self.histogram = Histogram()
        self.highscore: HighScore = HighScore()
        self.pvp = ["Player 1", "Player 2"]
        self.pvc = ["Player", "Jarvis AI"]
        self.turn_total = 0
        self.current_player_pvp = ""
        self.current_player_pvc = ""
        self.pvp_scores = {}
        self.pvc_scores = {}

    def switch_pvp(self) -> None:
        """Switch to the next player in PvP mode and reset the turn total."""

        self.current_player_pvp = (
            self.pvp[1]
            if self.current_player_pvp == self.pvp[0]
            else self.pvp[0]
        )
        self.turn_total = 0

    def switch_pvc(self) -> None:
        """Switch to the next participant in PvC mode and reset turn total."""

        self.current_player_pvc = (
            self.pvc[1]
            if self.current_player_pvc == self.pvc[0]
            else self.pvc[0]
        )
        self.turn_total = 0

    def game_mode(self) -> str: #pragma: no cover
        """Display and return the selected game mode (PvP or PvC)."""

        print("\n---------- Game Mode ----------") #pragma: no cover
        print("1. Player vs Player\n2. Player vs Computer")
        return input("Choose a game mode (1/2): ")

    def game_level(self) -> str:
        """Display and return the selected AI difficulty level."""

        print("\n---------- Game Level ----------")
        print("1. Easy\n2. Medium\n3. Hard")
        return input("Choose a game level (1/2/3): ")

    def double_one_pvp(self) -> None: #pragma: no cover
        """Handle the event of rolling double ones in PvP mode."""

        print(f"Turn total: {0}")
        print("\nDouble ones! You lose all your points.")
        self.pvp_scores[self.current_player_pvp] = 0

    def double_one_pvc(self) -> None:
        """Handle the event of rolling double ones in PvC mode."""

        print(f"Turn total: {0}")
        print("\nDouble ones! You lose all your points.")
        self.pvc_scores[self.current_player_pvc] = 0

    def add_turn_total(self, result: dict) -> None: #pragma: no cover
        """Add the result of a roll to the current turn total."""

        self.turn_total += result["total"]
        print(f"Turn total: {self.turn_total}")

    def roll(self) -> dict:
        """Roll dice for a human player and return the evaluated result."""

        input("\nPress Enter to roll...")
        result = self.dice_hand.evaluate_roll()
        print(f"Rolled: {self.dice_hand.display_dice()}")
        return result

    def computer_roll(self) -> dict: #pragma: no cover
        """Roll dice for the AI player and return the evaluated result."""

        result = self.dice_hand.evaluate_roll()
        print(f"\nRolled: {self.dice_hand.display_dice()}")
        return result

    def scoreboard(self, choice: str) -> None: #pragma: no cover
        """Display the current scoreboard depending on the game mode."""

        if choice == "1":
            p1_name = self.pvp[0]
            p1_score = [self.pvp_scores[self.pvp[0]]]
            p2_name = self.pvp[1]
            p2_score = [self.pvp_scores[self.pvp[1]]]
            print(
                f"\n----------- ScoreBoard ----------\n"
                f"""   {p1_name} {p1_score} - {p2_score} {p2_name}"""
            )
        elif choice == "2":
            p_name = self.pvc[0]
            p_score = [self.pvc_scores[self.pvc[0]]]
            ai_name = self.pvc[1]
            ai_score = [self.pvc_scores[self.pvc[1]]]
            print(
                f"\n----------- ScoreBoard ----------\n"
                f"""   {p_name} {p_score} - {ai_score} {ai_name}"""
            )

    def pause_menu(self) -> str: #pragma: no cover
        """Display the pause menu and return the selected option."""

        print("\n----- Paused -----")
        print("1. Continue\n2. Restart Game\n3. Change Name\n4. Quit Game")
        return input("Select an option (1/2/3/4): ")

    def pvp_play(self, user_choice: str) -> None: #pragma: no cover
        """Handle a full turn cycle for a single player in PvP mode."""

        self.scoreboard(user_choice)
        print(f"\n{self.current_player_pvp}'s turn:")
        while True:
            result = self.roll()
            if result["is_double_one"]:
                self.double_one_pvp()
                break

            if result["is_single_one"]:
                print(f"Turn total: {0}")
                print("\nRolled a single one. Turn ends with no points.")
                break

            self.add_turn_total(result)

            if result["must_reroll"]:
                print("\nRolled a pair! You must roll again.")
                continue

            if input("\nPause game? (p): ").strip().lower() == "p":
                option = self.pause_menu()
                if option == "1":
                    pass
                elif option == "2":
                    self.pvp_scores = {player: 0 for player in self.pvp}
                    self.turn_total = 0
                    self.current_player_pvp = ""
                    print("\nGame Restarted!")
                    break
                elif option == "3":
                    p_id = input("\nEnter your user ID: ")
                    name = input("Enter new name: ")
                    self.histogram.update_username(p_id, name)
                    score = self.pvp_scores[self.current_player_pvp]
                    self.pvp_scores.pop(self.current_player_pvp, None)
                    idx = self.pvp.index(self.current_player_pvp)
                    self.pvp.pop(idx)
                    self.pvp.insert(idx, name)
                    self.current_player_pvp = name
                    self.pvp_scores[name] = score
                    print("Changes saved.")
                elif option == "4":
                    print("\nAre you sure you want to quit? ")
                    select = input("All progress will be lost (y/n): ")
                    if select != "n":
                        self.pvp_scores = {player: 0 for player in self.pvp}
                        self.turn_total = 0
                        return "quit"

            if input("\nRoll again? (y/n): ").strip().lower() != "y":
                self.pvp_scores[self.current_player_pvp] += self.turn_total
                break

        self.switch_pvp()
        return None

    def pvc_play(self, user_choice: str, level: str) -> None: #pragma: no cover
        """Handle a full turn cycle in PvC mode, including AI decision logic."""

        self.scoreboard(user_choice)
        print(f"\n{self.current_player_pvc}'s turn:")
        ai_double_one = False
        ai_opt = ""
        while True:
            if self.current_player_pvc == self.pvc[1]:
                result = self.computer_roll()
            else:
                result = self.roll()

            if result["is_double_one"]:
                self.double_one_pvc()
                ai_double_one = self.current_player_pvc == self.pvc[1]
                break

            if result["is_single_one"]:
                print(f"Turn total: {0}")
                print("\nRolled a single one. Turn ends with no points.")
                break

            self.add_turn_total(result)

            if result["must_reroll"]:
                print("\nRolled a pair! You must roll again.")
                continue

            if self.current_player_pvc == self.pvc[0]:
                user_input = input("\nPause game? (p to pause, Enter to continue): ")
                if user_input.strip().lower() == "p":
                    option = self.pause_menu()
                    if option == "1":
                        pass
                    elif option == "2":
                        self.pvc_scores = {player: 0 for player in self.pvc}
                        self.turn_total = 0
                        self.current_player_pvc = ""
                        print("\nGame Restarted!")
                        break
                    elif option == "3":
                        p_id = input("\nEnter your user ID: ")
                        name = input("Enter new name: ")
                        self.histogram.update_username(p_id, name)
                        score = self.pvc_scores[self.pvc[0]]
                        self.pvc_scores.pop(self.pvc[0], None)
                        self.pvc.pop(0)
                        self.pvc.insert(0, name)
                        self.current_player_pvc = self.pvc[0]
                        self.pvc_scores[self.pvc[0]] = score
                        print("Changes saved.")

                    elif option == "4":
                        print("\nAre you sure you want to quit? ")
                        select = input("All progress will be lost (y/n): ")
                        if select != "n":
                            self.pvc_scores = {player: 0 for player in self.pvc}
                            self.turn_total = 0
                            return "quit"

                if input("\nRoll again? (y/n): ").strip().lower() != "y":
                    self.pvc_scores[self.current_player_pvc] += self.turn_total
                    break

            elif self.current_player_pvc == self.pvc[1]:
                if level == "1":
                    ai_opt = self.ai_lvl.easy(self.turn_total)
                elif level == "2":
                    ai_score = self.pvc_scores[self.pvc[1]]
                    ai_opt = self.ai_lvl.mid(self.turn_total, ai_score, ai_double_one)
                elif level == "3":
                    p_score = self.pvc_scores[self.pvc[0]]
                    ai_score = self.pvc_scores[self.pvc[1]]
                    ai_opt = self.ai_lvl.hard(self.turn_total, p_score, ai_score)

                if ai_opt != "y":
                    self.pvc_scores[self.current_player_pvc] += self.turn_total
                    break

        self.switch_pvc()
        return None

    def player_type(self) -> tuple: #pragma: no cover
        """
        Determine if the user is a new or
        returning player and return ID +
        username.
        """

        print("1. New Player\n2. Existing Player")
        choice = input("Select an option (1/2): ")
        if choice == "1":
            input_id = input("\nEnter a new user ID Player e.g. Mar580: ")
            while input_id in self.player.get_user_id_list():
                input_id = input("\nUser ID Exists!\nEnter new ID: ")
            self.player.set_id(input_id)
            user_id = self.player.get_user_id()
            self.player.set_username(input("Enter your name Player: "))
            username = self.player.get_username()
            self.histogram.update_username(user_id, username)
            return user_id, username
        if choice == "2":
            print(
                "\nINFO: Make sure to enter an existing ID on your first try,"
                " otherwise you will be asked to create a new one."
            )
            input_id = input("\nEnter your existing user ID Player e.g. Mar580: ")
            if input_id in self.player.get_user_id_list():
                self.player.set_id(input_id)
                user_id = self.player.get_user_id()
                username = self.histogram.get_username(user_id)
                return user_id, username

            print("User ID Does Not Exist!\n")
            input_id = input("Enter a new user ID Player e.g. Mar580: ")
            while input_id in self.player.get_user_id_list():
                input_id = input("User ID Exists!\nEnter new ID: ")
            self.player.set_id(input_id)
            user_id = self.player.get_user_id()
            self.player.set_username(input("Enter your name Player: "))
            username = self.player.get_username()
            self.histogram.update_username(user_id, username)
            return user_id, username
        return None, None

    def save_pvp1(self, p_id: str, winner: str) -> None: #pragma: no cover
        """Save stats for PvP player 1 after a completed match."""

        self.histogram.increment_games_played(p_id)
        if winner == self.pvp[0]:
            self.histogram.increment_games_won(p_id)
        else:
            self.histogram.increment_games_lost(p_id)
        self.highscore.set_highscore(self.pvp_scores[self.pvp[0]])
        score = self.highscore.get_highscore()
        self.histogram.check_highscore(p_id, score)
        self.histogram.save_stats()

    def save_pvp2(self, p_id: str, winner: str) -> None: #pragma: no cover
        """Save stats for PvP player 2 after a completed match."""

        self.histogram.increment_games_played(p_id)
        if winner == self.pvp[1]:
            self.histogram.increment_games_won(p_id)
        else:
            self.histogram.increment_games_lost(p_id)
        self.highscore.set_highscore(self.pvp_scores[self.pvp[1]])
        score = self.highscore.get_highscore()
        self.histogram.check_highscore(p_id, score)
        self.histogram.save_stats()

    def save_pvc1(self, p_id: str, winner: str) -> None:
        """Save stats for the player in Player vs Computer mode."""

        self.histogram.increment_games_played(p_id)
        if winner == self.pvc[0]:
            self.histogram.increment_games_won(p_id)
        else:
            self.histogram.increment_games_lost(p_id) #pragma: no cover
        self.highscore.set_highscore(self.pvc_scores[self.pvc[0]])
        score = self.highscore.get_highscore()
        self.histogram.check_highscore(p_id, score)
        self.histogram.save_stats()

    def start_pvp_game(self, choice: str) -> None: #pragma: no cover
        """Set up and run a full Player vs Player match."""

        print("\n------- Player Selection -------")
        print("\n>>> Player 1\n")
        p1_id, p1_username = self.player_type()
        self.pvp[0] = p1_username
        print("\n>>> Player 2\n")
        p2_id, p2_username = self.player_type()
        self.pvp[1] = p2_username
        self.current_player_pvp = self.pvp[0]
        self.pvp_scores: dict[str, int] = {player: 0 for player in self.pvp}
        pause_menu_option = ""
        while max(self.pvp_scores.values()) < 100:
            pause_menu_option = self.pvp_play(choice)
            if pause_menu_option == "quit":
                break
        if pause_menu_option != "quit":
            self.scoreboard(choice)
            winner = max(self.pvp_scores, key=self.pvp_scores.get)
            self.save_pvp1(p1_id, winner)
            self.save_pvp2(p2_id, winner)
            print(f"\n🎉 {winner} wins with {self.pvp_scores[winner]} points!")

    def start_pvc_game(self, choice: str) -> None: #pragma: no cover
        """Set up and run a full Player vs Computer match."""

        print("\n------- Player Selection -------")
        user_id, username = self.player_type()
        self.pvc[0] = username
        self.pvc_scores: dict[str, int] = {player: 0 for player in self.pvc}
        self.current_player_pvc = self.pvc[0]
        level = self.game_level()
        pause_menu_option = ""
        while max(self.pvc_scores.values()) < 100:
            pause_menu_option = self.pvc_play(choice, level)
            if pause_menu_option == "quit":
                break

        if pause_menu_option != "quit":
            self.scoreboard(choice)
            winner = max(self.pvc_scores, key=self.pvc_scores.get)
            self.save_pvc1(user_id, winner)
            print(f"\n🎉 {winner} wins with {self.pvc_scores[winner]} points!")

    def start_game(self) -> None: #pragma: no cover
        """Start and manage the overall game flow including mode selection."""

        choice = self.game_mode()
        if choice == "1":
            self.start_pvp_game(choice)

        elif choice == "2":
            self.start_pvc_game(choice)
