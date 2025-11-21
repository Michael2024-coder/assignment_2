"""
Simple unit tests for the Player class.

These tests cover username and user ID handling.
"""

import unittest
import pickle
from dice.player import Player


class TestPlayer(unittest.TestCase):
    """Test suite for verifying Player class functionality."""

    def setUp(self):
        """Prepare an empty user_id.ser file and create Player objects."""
        # Make sure the ID file exists and contains an empty set
        with open("dice/user_id.ser", "wb") as f:
            pickle.dump(set(), f)

        # Create simple Player objects
        self.p1 = Player()
        self.p2 = Player()
        self.p3 = Player()

    def test_set_username(self):
        """Test setting a username."""
        self.p1.set_username("Michael")
        self.assertEqual(self.p1.get_username(), "Michael")

    def test_set_id(self):
        """Test setting a new user ID."""
        self.p2.set_id("ID001")
        self.assertEqual(self.p2.get_user_id(), "ID001")
        self.assertIn("ID001", self.p2.user_id_list)

    def test_set_multiple_ids(self):
        """Test that multiple players do not overwrite each other's IDs."""
        self.p1.set_id("A1")
        self.p2.set_id("B2")

        self.assertEqual(self.p1.get_user_id(), "A1")
        self.assertEqual(self.p2.get_user_id(), "B2")

    def test_username_starts_empty(self):
        """Test that username is initially empty."""
        self.assertEqual(self.p3.get_username(), "")

if __name__ == "__main__":
    unittest.main()
