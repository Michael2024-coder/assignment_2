"""Main game controller for the Two-Dice Pig game."""

from __future__ import annotations
import sys
from pathlib import Path

from dice.dice_hand import DiceHand


class Game:
    """Main game controller for Two-Dice Pig."""

    def __init__(self) -> None:
        """Initialize the game with players, scores, and dice."""
        self.dice_hand = DiceHand()
        self.players = ["Player 1", "Player 2"]
        self.scores: dict[str, int] = {player: 0 for player in self.players}
        self.current_player = self.players[0]
        self.turn_total = 0

    def switch_player(self) -> None:
        """Switch to the next player and reset turn total."""
        self.current_player = (
            self.players[1]
            if self.current_player == self.players[0]
            else self.players[0]
        )
        self.turn_total = 0

    def play_turn(self) -> None:
        """Play a single turn for the current player."""
        print(f"\n{self.current_player}'s turn:")
        while True:
            input("Press Enter to roll...")
            result = self.dice_hand.evaluate_roll()
            print(f"Rolled: {self.dice_hand.display_dice()}")

            if result["is_double_one"]:
                print("Double ones! You lose all your points.")
                self.scores[self.current_player] = 0
                break

            if result["is_single_one"]:
                print("Rolled a single one. Turn ends with no points.")
                break

            self.turn_total += result["total"]
            print(f"Turn total: {self.turn_total}")

            if result["must_reroll"]:
                print("Rolled a pair! You must roll again.")
                continue

            choice = input("Roll again? (y/n): ").strip().lower()
            if choice != "y":
                self.scores[self.current_player] += self.turn_total
                print(
                    f"{self.current_player}'s total score: "
                    f"{self.scores[self.current_player]}"
                )
                break

        self.switch_player()

    def start_game(self) -> None:
        """Start and manage the full game loop."""
        print("Welcome to Two-Dice Pig!")
        while max(self.scores.values()) < 100:
            self.play_turn()

        winner = max(self.scores, key=self.scores.get)
        print(f"\n🎉 {winner} wins with {self.scores[winner]} points!")


if __name__ == "__main__":
    # Allow running directly from VS Code or terminal
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    GAME = Game()
    GAME.start_game()
