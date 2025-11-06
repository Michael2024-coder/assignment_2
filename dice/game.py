"""Main game controller for the Two-Dice Pig game."""

from __future__ import annotations
import sys
from pathlib import Path

from dice.dice_hand import DiceHand
from dice.intelligence import Intelligence

class Game:
    """Main game controller for Two-Dice Pig."""

    def __init__(self) -> None:
        """Initialize the game with players, scores, and dice."""
        self.dice_hand = DiceHand()
        self.computer_intelligence = Intelligence()
        self.pvp = ["Player 1", "Player 2"]
        self.pvc = ["Player", "Computer"]
        self.pvp_scores: dict[str, int] = {player: 0 for player in self.pvp}
        self.pvc_scores: dict[str, int] = {player: 0 for player in self.pvc}
        self.current_player_pvp = self.pvp[0]
        self.current_player_pvc = self.pvc[0]
        self.turn_total = 0

    def switch_pvp(self) -> None:
        """Switch to the next player and reset turn total."""
        self.current_player_pvp = (
            self.pvp[1]
            if self.current_player_pvp == self.pvp[0]
            else self.pvp[0]
        )
        self.turn_total = 0
        
    def switch_pvc(self) -> None:
        self.current_player_pvc = (
            self.pvc[1]
            if self.current_player_pvc == self.pvc[0]
            else self.pvc[0]
        )
        self.turn_total = 0

    def game_mode(self) -> str:
        print("---------- Game Mode ----------")
        print("1. Player vs Player\n2. Player vs Computer")
        return input("Choose a game mode (1/2): ")
        
    def game_level(self) -> str:
        print("\n---------- Game Level ----------")
        print("1. Easy\n2. Medium\n3. Hard")
        return input("Choose a game level (1/2/3): ")
        
    def double_one_pvp(self) -> None:
        print("\nDouble ones! You lose all your points.")
        self.pvp_scores[self.current_player_pvp] = 0
        
    def double_one_pvc(self) -> None:
        print(f"Turn total: {0}")
        print("\nDouble ones! You lose all your points.")
        self.pvc_scores[self.current_player_pvc] = 0
        
    def single_one(self) -> None:
        print(f"Turn total: {0}")
        print("\nRolled a single one. Turn ends with no points.")
            
    def must_reroll(self) -> None:
        print("\nRolled a pair! You must roll again.")
            
    def add_turn_total(self, result) -> None:
        self.turn_total += result["total"]
        print(f"Turn total: {self.turn_total}")
        
    def roll(self) -> dict:
        input("\nPress Enter to roll...")
        result = self.dice_hand.evaluate_roll()
        print(f"Rolled: {self.dice_hand.display_dice()}")
        return result
    
    def computer_roll(self) -> dict:
        result = self.dice_hand.evaluate_roll()
        print(f"\nRolled: {self.dice_hand.display_dice()}")
        return result
    
    def stop_turn_pvp(self) -> None:
        self.pvp_scores[self.current_player_pvp] += self.turn_total
        
    def stop_turn_pvc(self) -> None:
        self.pvc_scores[self.current_player_pvc] += self.turn_total
        
    def scoreboard(self, choice) -> None:
        if choice == "1":
            print(
                f"\n----------- ScoreBoard ----------\n"
                f"   {self.pvp[0]} {[self.pvp_scores[self.pvp[0]]]} - {[self.pvp_scores[self.pvp[1]]]} {self.pvp[1]}"
            )
        elif choice == "2":
            print(
                f"\n----------- ScoreBoard ----------\n"
                f"    {self.pvc[0]} {[self.pvc_scores[self.pvc[0]]]} - {[self.pvc_scores[self.pvc[1]]]} {self.pvc[1]}"
            )
            
    def pvp_play(self, user_choice) -> None:
        """Play a single turn for the current player."""
        self.scoreboard(user_choice)
        print(f"\n{self.current_player_pvp}'s turn:")
        while True:
            result = self.roll()

            if result["is_double_one"]:
                self.double_one_pvc()
                break
            
            if result["is_single_one"]:
                self.single_one()
                break
            
            self.add_turn_total(result)
            
            if result["must_reroll"]:
                self.must_reroll()
                continue

            choice = input("\nRoll again? (y/n): ").strip().lower()
            if choice != "y":
                self.stop_turn_pvp()
                break

        self.switch_pvp()
    
    def pvc_play(self, user_choice, level) -> None:
        self.scoreboard(user_choice)
        print(f"\n{self.current_player_pvc}'s turn:")
        comp_double_one = False
        while True:
            if self.current_player_pvc == "Computer":
                result = self.computer_roll()
            else:
                result = self.roll()

            if result["is_double_one"]:
                self.double_one_pvc()
                if self.current_player_pvc == "Computer":
                    comp_double_one = True
                break
            
            if result["is_single_one"]:
                self.single_one()
                break
            
            self.add_turn_total(result)
            
            if result["must_reroll"]:
                self.must_reroll()
                continue

            if self.current_player_pvc == "Player":
                choice = input("\nRoll again? (y/n): ").strip().lower()
                if choice != "y":
                    self.stop_turn_pvc()
                    break
            
            elif self.current_player_pvc == "Computer":
                if level == "1":
                    choice = self.computer_intelligence.easy_level(self.turn_total)
                elif level == "2":
                    choice = self.computer_intelligence.medium_level(self.turn_total, self.pvc_scores["Computer"], comp_double_one)
                elif level == "3":
                    choice = self.computer_intelligence.hard_level(self.turn_total, self.pvc_scores["Player"], self.pvc_scores["Computer"])
                    
                if choice != "y":
                    self.stop_turn_pvc()
                    break
                
        self.switch_pvc()

    def start_game(self) -> None:
        """Start and manage the full game loop."""
        print("\n---------- Welcome to Two-Dice Pig! ----------\n")
        choice = self.game_mode()
        
        if choice == "1":
            while max(self.pvp_scores.values()) < 100:
                self.pvp_play(choice)
                
            self.scoreboard(choice)
            winner = max(self.pvp_scores, key=self.pvp_scores.get)
            print(f"\n🎉 {winner} wins with {self.pvp_scores[winner]} points!")
        
        elif choice == "2":
            level = self.game_level()
            while max(self.pvc_scores.values()) < 100:
                self.pvc_play(choice, level)
                
            self.scoreboard(choice)
            winner = max(self.pvc_scores, key=self.pvc_scores.get)
            print(f"\n🎉 {winner} wins with {self.pvc_scores[winner]} points!")


if __name__ == "__main__":
    # Allow running directly from VS Code or terminal
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    GAME = Game()
    GAME.start_game()
