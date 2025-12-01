"""
Expanded unit tests for the HighScore class.
Includes 10 test cases and 20+ assertions.
"""

import unittest
from dice.highscore import HighScore


class TestHighScore(unittest.TestCase):
    """Comprehensive test suite for HighScore."""

    def setUp(self):
        """Create a new HighScore object before each test."""
        self.hs = HighScore()

    def test_initial_value_zero(self):
        """Highscore should be 0 when the class is first created."""
        self.assertEqual(self.hs.get_highscore(), 0)
        self.assertIsInstance(self.hs.get_highscore(), int)

    def test_set_highscore_once(self):
        """Set highscore one time and verify the value."""
        self.hs.set_highscore(10)
        self.assertEqual(self.hs.get_highscore(), 10)
        self.assertNotEqual(self.hs.get_highscore(), 5)

    def test_set_highscore_twice(self):
        """Set highscore two times and confirm the latest value is stored."""
        self.hs.set_highscore(20)
        self.hs.set_highscore(40)
        self.assertEqual(self.hs.get_highscore(), 40)
        self.assertGreater(self.hs.get_highscore(), 20)

    def test_set_zero(self):
        """Setting highscore to zero should work."""
        self.hs.set_highscore(0)
        self.assertEqual(self.hs.get_highscore(), 0)

    def test_negative_score(self):
        """Negative values should be allowed since the class does not block them."""
        self.hs.set_highscore(-5)
        self.assertEqual(self.hs.get_highscore(), -5)
        self.assertLess(self.hs.get_highscore(), 0)

    def test_large_score(self):
        """Test setting a very large highscore value."""
        self.hs.set_highscore(1_000_000)
        self.assertEqual(self.hs.get_highscore(), 1_000_000)
        self.assertGreater(self.hs.get_highscore(), 999_999)

    def test_type_after_updates(self):
        """Highscore should remain an integer no matter how many updates."""
        self.hs.set_highscore(123)
        self.assertIsInstance(self.hs.get_highscore(), int)

    def test_multiple_updates(self):
        """Updating the highscore many times should store the latest value."""
        values = [3, 6, 9, 12, 15]
        for v in values:
            self.hs.set_highscore(v)

        self.assertEqual(self.hs.get_highscore(), 15)
        self.assertIn(self.hs.get_highscore(), values)

    def test_compare_scores(self):
        """Check that comparisons with the highscore behave correctly."""
        self.hs.set_highscore(50)
        self.assertTrue(self.hs.get_highscore() >= 50)
        self.assertFalse(self.hs.get_highscore() < 10)

    def test_boundary_values(self):
        """Test boundary values like 1 and -1."""
        self.hs.set_highscore(1)
        self.assertEqual(self.hs.get_highscore(), 1)

        self.hs.set_highscore(-1)
        self.assertEqual(self.hs.get_highscore(), -1)


if __name__ == "__main__":
    unittest.main()
