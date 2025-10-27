"""Module defining the Dice class for rolling and displaying a single die."""

import random


class Dice:
    """Represents a single die with roll functionality and UTF-8 graphics."""

    DICE_UNICODE = {
        1: "\u2680",  # ⚀
        2: "\u2681",  # ⚁
        3: "\u2682",  # ⚂
        4: "\u2683",  # ⚃
        5: "\u2684",  # ⚄
        6: "\u2685",  # ⚅
    }

    def __init__(self, sides: int = 6) -> None:
        """Initialize the die with a given number of sides (default is 6)."""
        self.sides = sides
        self.value: int | None = None

    def roll(self) -> int:
        """Roll the die and return the result."""
        self.value = random.randint(1, self.sides)
        return self.value

    def get_unicode(self) -> str:
        """Return the UTF-8 symbol for the current face value."""
        return self.DICE_UNICODE.get(self.value, "[?]")

    def __str__(self) -> str:
        """Return the UTF-8 representation of the die face."""
        return self.get_unicode()
