"""
Intelligence module for computer decision-making in a turn-based dice game.

This module provides the `Intelligence` class, which implements AI logic
for three difficulty levels:

- Easy: Rolls until a safe turn threshold (20 points) is reached.
- Medium: Adapts roll behavior based on previous scores, allowed turns,
    and special conditions such as double ones.
- Hard: Uses dynamic strategies based on player and computer scores,
    late-game scenarios, and score differences.

The class methods return 'y' to continue rolling or 'n' to stop.
"""


class Intelligence:
    """
    A class that implements decision-making logic for three difficulty levels.

    (easy, medium, and hard) in a turn-based dice game.
    """

    def __init__(self):  # pragma: no cover
        """
        Initialize the Intelligence object.

        Attributes:
            medium_turn_count (int): Counter controlling
            behavior for the medium difficulty level.

            score_list (list): Tracks previous scores
            encountered in medium difficulty logic.
        """
        self.medium_turn_count = 5
        self.score_list = []

    def easy(self, turn_total: int) -> str:  # pragma: no cover
        """
        Decision logic for the easy difficulty level.

        Parameters:
            turn_total (int): The current accumulated total for the turn.

        Returns:
            str: 'y' to continue rolling, 'n' to stop rolling.
        """
        if turn_total >= 20:
            return 'n'
        return 'y'

    def mid(
            self, turn_total: int,
            score: int,
            comp_double_one: bool
            ) -> str:  # pragma: no cover
        """
        Decision logic for the medium difficulty level.

        Behavior adapts based on previously seen scores, remaining allowed turns,
        and special conditions such as the computer rolling double ones.

        Parameters:
            turn_total (int): The current accumulated total for the turn.
            score (int): The computer's running score for the game.
            comp_double_one (bool): Whether the computer rolled
            double ones in this turn.

        Returns:
            str: 'y' to continue rolling, 'n' to stop rolling.
        """
        if score not in self.score_list:
            self.medium_turn_count -= 1
            self.score_list.append(score)

        if comp_double_one:
            self.medium_turn_count = 5
            self.score_list = []

        if self.medium_turn_count > 0 and self.medium_turn_count < 4:
            remainder = int((100 - score) / self.medium_turn_count)
            if turn_total >= remainder:
                return 'n'
            return 'y'

        if self.medium_turn_count == 4:
            if turn_total >= 25:
                return 'n'
            return 'y'
        return None

    def hard(
            self, turn_total: int,
            player_score: int,
            computer_score: int
            ) -> str:  # pragma: no cover
        """
        Decision logic for the hard difficulty level.

        The computer adapts based on score differences, player advantage,
        and late-game risk management.

        Parameters:
            turn_total (int): The current accumulated total for the turn.
            player_score (int): The player's current score.
            computer_score (int): The computer's current score.

        Returns:
            str: 'y' to continue rolling, 'n' to stop rolling.
        """
        if player_score >= 71 or computer_score >= 71:
            if turn_total >= 100 - computer_score:
                return 'n'
            return 'y'

        score_diff = 0
        if player_score > computer_score:
            score_diff = player_score - computer_score
        elif computer_score > player_score:
            score_diff = computer_score - player_score

        if turn_total >= int(21 + (score_diff / 8)):
            return 'n'
        return 'y'
