"""
Unit tests for the Player class.

These tests cover username validation, score resetting, and initial game statistics.
"""

import unittest
from dice.Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Michael")
        self.p2 = Player("Ngozi")
        self.p3 = Player("Apan")

    def test_initial_stats(self):
        stats = self.p1.get_stats()
        self.assertEqual(stats["score"], 0)
        self.assertEqual(stats["games_played"], 0)

    def test_change_username_valid(self):
        self.p2.change_username("Big Mike")
        self.assertEqual(self.p2.get_username(), "Big Mike")

    def test_change_username_invalid(self):
        # No alphabetic characters — should raise ValueError
        with self.assertRaises(ValueError):
            self.p3.change_username("876")

    def test_score_reset(self):
        self.p2.current_score = 50
        self.p2.reset_score()
        self.assertEqual(self.p2.current_score, 0)


if __name__ == "__main__":
    unittest.main()
