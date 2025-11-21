"""
Unit tests for the HighScore class.
"""

import unittest
from dice.highscore import HighScore


class TestHighScore(unittest.TestCase):
    """Test suite for the HighScore class."""

    def setUp(self):
        """Initialize a fresh HighScore instance before each test."""
        self.hs = HighScore()

    def test_initial_highscore(self):
        """Test that the initial high score is zero."""
        self.assertEqual(self.hs.get_highscore(), 0, "Initial high score should be 0")

    def test_set_and_get_highscore(self):
        """Test that setting a high score works correctly."""
        self.hs.set_highscore(50)
        self.assertEqual(
            self.hs.get_highscore(), 50,
            "High score should be updated to 50"
            )

        self.hs.set_highscore(100)
        self.assertEqual(
            self.hs.get_highscore(), 100,
            "High score should be updated to 100"
            )


if __name__ == "__main__":
    unittest.main()
