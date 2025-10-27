"""Module for managing a pair of dice in the Two-Dice Pig game."""

from dice.dice_class import Dice


class DiceHand:
    """Manages two dice and evaluates roll outcomes for Two-Dice Pig."""

    def __init__(self) -> None:
        """Initialize the DiceHand with two dice."""
        self.left_die = Dice()
        self.right_die = Dice()

    def roll(self) -> tuple[int, int]:
        """Roll both dice and return their values."""
        left_value = self.left_die.roll()
        right_value = self.right_die.roll()
        return left_value, right_value
       
    def evaluate_roll(self) -> dict[str, object]:
        """Evaluate the result of the roll according to game rules."""
        left_value, right_value = self.roll()
        is_pair = left_value == right_value
        return {
            "face_values": (left_value, right_value),
            "total": left_value + right_value,
            "is_pair": is_pair,
            "is_single_one": (
                1 in (left_value, right_value) and left_value != right_value
            ),
            "is_double_one": left_value == right_value == 1,
            "must_reroll": is_pair and left_value != 1,
        }

    def display_dice(self) -> str:
        """Return a string showing both dice graphically."""
        return f"{self.left_die} {self.right_die}"
