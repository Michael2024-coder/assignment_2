"""
Expanded unit tests for the Player class.

These tests now include 10 test methods and 20+ assertions.
"""

import unittest
import pickle
from dice.player import Player


class TestPlayer(unittest.TestCase):
    """Comprehensive test suite for the Player class."""

    def setUp(self):
        """Reset user_id.ser before each test."""
        with open("dice/user_id.ser", "wb") as f:
            pickle.dump(set(), f)

        self.p1 = Player()
        self.p2 = Player()
        self.p3 = Player()

    def test_username_default(self):
        """Username should start empty."""
        self.assertEqual(self.p1.get_username(), "")
        self.assertEqual(self.p2.get_username(), "")
        self.assertEqual(self.p3.get_username(), "")

    def test_set_username(self):
        """Set username and verify it."""
        self.p1.set_username("Michael")
        self.assertEqual(self.p1.get_username(), "Michael")
        self.p2.set_username("Anna")
        self.assertEqual(self.p2.get_username(), "Anna")

    def test_unique_ids(self):
        """Players should not share IDs."""
        self.p1.set_id("X1")
        self.p2.set_id("Y2")
        self.assertNotEqual(self.p1.get_user_id(), self.p2.get_user_id())
        self.assertEqual(self.p1.get_user_id(), "X1")
        self.assertEqual(self.p2.get_user_id(), "Y2")

    def test_id_saved_to_file(self):
        """Check if ID is saved in the file."""
        self.p1.set_id("A10")

        with open("dice/user_id.ser", "rb") as f:
            ids = pickle.load(f)

        self.assertIn("A10", ids)
        self.assertIsInstance(ids, set)

    def test_multiple_ids_saved(self):
        """Multiple players should save IDs."""
        self.p1.set_id("A1")
        self.p2.set_id("B2")
        self.p3.set_id("C3")

        with open("dice/user_id.ser", "rb") as f:
            ids = pickle.load(f)

        self.assertEqual(len(ids), 3)
        self.assertIn("A1", ids)
        self.assertIn("B2", ids)
        self.assertIn("C3", ids)

    def test_duplicate_id_not_duplicated(self):
        """Duplicate IDs should not create extra entries."""
        self.p1.set_id("XX")
        self.p2.set_id("XX")  # same ID

        with open("dice/user_id.ser", "rb") as f:
            ids = pickle.load(f)

        self.assertEqual(len(ids), 1)
        self.assertIn("XX", ids)

    def test_get_user_id(self):
        """Test ID retrieval."""
        self.p1.set_id("T9")
        self.assertEqual(self.p1.get_user_id(), "T9")
        self.assertNotEqual(self.p1.get_user_id(), "Wrong")

    def test_user_id_list_type(self):
        """user_id_list should be a set."""
        self.assertIsInstance(self.p1.user_id_list, (set, list))

    def test_username_string_type(self):
        """Usernames must be strings."""
        self.p1.set_username("Mark")
        self.assertIsInstance(self.p1.get_username(), str)

    def test_id_string_type(self):
        """IDs must be strings."""
        self.p2.set_id("ID77")
        self.assertIsInstance(self.p2.get_user_id(), str)
        self.assertNotIsInstance(self.p2.get_user_id(), int)


if __name__ == "__main__":
    unittest.main()
