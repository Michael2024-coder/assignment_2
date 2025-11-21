"""
Unit tests for the Intelligence class in the dice game AI module.

Tests decision-making logic for easy, medium, and hard difficulty levels.
"""

import unittest
from dice.intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Test suite for the Intelligence decision-making logic."""

    def setUp(self):
        """Initialize a fresh Intelligence instance before each test."""
        self.ai = Intelligence()

    def test_easy_decision(self):
        """Test easy AI decision logic based on turn total."""
        self.assertEqual(self.ai.easy(10), 'y', "Should continue rolling if below 20")
        self.assertEqual(self.ai.easy(20), 'n', "Should stop rolling at 20")
        self.assertEqual(self.ai.easy(25), 'n', "Should stop rolling above 20")

    def test_mid_decision_no_double_one(self):
        """Test medium AI decision logic without double ones."""
        # initial call, medium_turn_count starts at 5
        result = self.ai.mid(turn_total=5, score=10, comp_double_one=False)
        self.assertIn(result, ['y', 'n'], "Should return 'y' or 'n'")

        # simulate another call with same score to check behavior
        self.ai.medium_turn_count = 3
        result2 = self.ai.mid(turn_total=20, score=10, comp_double_one=False)
        self.assertIn(result2, ['y', 'n'], "Should return 'y' or 'n'")

    def test_mid_decision_with_double_one(self):
        """Test medium AI resets when double ones occur."""
        self.ai.medium_turn_count = 2
        self.ai.score_list = [5, 10]
        self.ai.mid(turn_total=10, score=10, comp_double_one=True)

        # Check that score_list is reset
        self.assertEqual(self.ai.score_list, [], "Score list should be reset")
        # Check that medium_turn_count is reset to 5
        self.assertEqual(
            self.ai.medium_turn_count, 5,
            "Medium turn count should reset to 5"
            )

    def test_hard_decision_late_game(self):
        """Test hard AI decision logic near winning score."""
        # computer close to winning
        self.assertEqual(
            self.ai.hard(turn_total=10, player_score=70, computer_score=80),
            'y',
            "Should continue rolling if turn_total < remaining points"
        )
        self.assertEqual(
            self.ai.hard(turn_total=20, player_score=70, computer_score=80),
            'n',
            "Should stop rolling if turn_total >= remaining points"
        )

    def test_hard_decision_score_diff(self):
        """Test hard AI decision logic with normal scores and score differences."""
        self.assertEqual(
            self.ai.hard(turn_total=5, player_score=30, computer_score=20),
            'y',
            "Should continue rolling if below calculated threshold"
        )
        self.assertEqual(
            self.ai.hard(turn_total=25, player_score=30, computer_score=20),
            'n',
            """
            Should stop rolling if turn_total exceeds threshold based on
            score difference
            """
        )


if __name__ == "__main__":
    unittest.main()
