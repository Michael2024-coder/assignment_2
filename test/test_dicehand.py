"""Unit tests for the DiceHand class with mocked dice rolls."""

import unittest
from unittest.mock import patch
from dice.dice_hand import DiceHand


class TestDiceHand(unittest.TestCase):
    """Test suite for DiceHand with deterministic dice rolls."""

    def setUp(self) -> None:
        """Create a DiceHand instance before each test."""
        self.hand = DiceHand()

    @patch("dice.dice_class.Dice.roll")
    def test_double_one(self, mock_roll) -> None:
        """Test the double one scenario."""
        mock_roll.side_effect = [1, 1]
        result = self.hand.evaluate_roll()
        self.assertTrue(result["is_double_one"])
        self.assertEqual(result["total"], 2)
        self.assertFalse(result["must_reroll"])
        self.assertFalse(result["is_single_one"])

    @patch("dice.dice_class.Dice.roll")
    def test_single_one(self, mock_roll) -> None:
        """Test the single one scenario."""
        mock_roll.side_effect = [1, 3]
        result = self.hand.evaluate_roll()
        self.assertTrue(result["is_single_one"])
        self.assertFalse(result["is_double_one"])
        self.assertFalse(result["must_reroll"])

    @patch("dice.dice_class.Dice.roll")
    def test_pair_must_reroll(self, mock_roll) -> None:
        """Test a pair that is not double one (must reroll)."""
        mock_roll.side_effect = [4, 4]
        result = self.hand.evaluate_roll()
        self.assertTrue(result["is_pair"])
        self.assertFalse(result["is_double_one"])
        self.assertFalse(result["is_single_one"])
        self.assertTrue(result["must_reroll"])
        self.assertEqual(result["total"], 8)

    @patch("dice.dice_class.Dice.roll")
    def test_normal_roll(self, mock_roll) -> None:
        """Test a normal roll with no ones and no reroll."""
        mock_roll.side_effect = [2, 5]
        result = self.hand.evaluate_roll()
        self.assertFalse(result["is_double_one"])
        self.assertFalse(result["is_single_one"])
        self.assertFalse(result["must_reroll"])
        self.assertEqual(result["total"], 7)
        self.assertFalse(result["is_pair"])

    @patch("dice.dice_class.Dice.roll")
    def test_display_dice(self, mock_roll) -> None:
        """Test display_dice returns the correct Unicode string."""
        mock_roll.side_effect = [3, 6]
        self.hand.roll()  # set the dice values
        display = self.hand.display_dice()
        self.assertEqual(display, f"{self.hand.left_die} {self.hand.right_die}")


if __name__ == "__main__":
    unittest.main()
