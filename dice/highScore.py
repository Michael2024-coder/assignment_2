"""HighScore module for managing player scores and stats."""


class HighScore:
    """Tracks players, scores, and game statistics."""

    def __init__(self):
        """Initialize an empty high score value."""
        self.high_score = 0

    def set_highscore(self, score: int) -> None:
        """
        Set the current high score.

        Args:
            score (int): The score to set as the new high score.
        """
        self.high_score = score

    def get_highscore(self) -> int:
        """
        Retrieve the current high score.

        Returns:
            int: The stored high score value.
        """
        return self.high_score
