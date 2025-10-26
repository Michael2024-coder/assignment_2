"""Unit tests for the Player class.

These tests cover username validation, score resetting, and initial game statistics.
"""

import unittest
from dice.player import Player


class TestPlayer(unittest.TestCase):
    """Test suite for verifying Player class functionality."""

    def setUp(self):
        """Initialize sample players for testing."""
        self.p1 = Player("Michael")
        self.p2 = Player("Ngozi")
        self.p3 = Player("Apan")

    def test_initial_stats(self):
        """Test that initial stats are set to zero."""
        stats = self.p1.get_stats()
        self.assertEqual(stats["score"], 0)
        self.assertEqual(stats["games_played"], 0)

    def test_change_username_valid(self):
        """Test that a valid username change is applied correctly."""
        self.p2.change_username("Big Mike")
        self.assertEqual(self.p2.get_username(), "Big Mike")

    def test_change_username_invalid(self):
        """Test that an invalid username raises ValueError."""
        with self.assertRaises(ValueError):
            self.p3.change_username("876")

    def test_score_reset(self):
        """Test that reset_score sets current_score to zero."""
        self.p2.current_score = 50
        self.p2.reset_score()
        self.assertEqual(self.p2.current_score, 0)


if __name__ == "__main__":
    unittest.main()
