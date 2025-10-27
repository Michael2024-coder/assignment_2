"""Unit tests for the Dice class with deterministic rolls."""

import unittest
from unittest.mock import patch
from dice.dice_class import Dice


class TestDice(unittest.TestCase):
    """Test suite for the Dice class."""

    def setUp(self) -> None:
        """Create a Dice instance before each test."""
        self.dice = Dice()

    @patch("random.randint")
    def test_roll_returns_expected_value(self, mock_randint) -> None:
        """Rolling the die returns the mocked value."""
        mock_randint.return_value = 4
        value = self.dice.roll()
        self.assertEqual(value, 4)
        self.assertEqual(self.dice.value, 4)

    @patch("random.randint")
    def test_roll_range(self, mock_randint) -> None:
        """Rolling multiple times returns values between 1 and 6."""
        for expected in range(1, 7):
            mock_randint.return_value = expected
            value = self.dice.roll()
            self.assertEqual(value, expected)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)

    def test_get_unicode_returns_correct_symbol(self) -> None:
        """get_unicode() returns the correct UTF-8 symbol for each face."""
        for face, symbol in Dice.DICE_UNICODE.items():
            self.dice.value = face
            self.assertEqual(self.dice.get_unicode(), symbol)

    def test_str_returns_unicode(self) -> None:
        """__str__() returns the same value as get_unicode()."""
        for face in range(1, 7):
            self.dice.value = face
            self.assertEqual(str(self.dice), self.dice.get_unicode())


if __name__ == "__main__":
    unittest.main()
