"""
Unit tests for the Histogram class.

These tests mock file I/O operations to prevent reading/writing
real files and ensure deterministic, isolated testing.
"""

import unittest
from unittest.mock import mock_open, patch

from dice.histogram import Histogram


class TestHistogram(unittest.TestCase):
    """Tests for the Histogram class."""

    def setUp(self):
        """Set up a Histogram instance with mocked file loading."""
        self.mock_data = {
            "player1": {
                "Username": "John",
                "Highscore": 50,
                "Games_Played": 5,
                "Games_Won": 3,
                "Games_Lost": 2
            }
        }

        # Mock pickle.load to return mock_data
        with patch("builtins.open", mock_open(read_data=b"data")), \
                patch("pickle.load", return_value=self.mock_data):
            self.hist = Histogram()

    def test_increment_games_played(self):
        """Test incrementing games played."""
        self.hist.increment_games_played("player1")
        self.assertEqual(self.hist.details["player1"]["Games_Played"], 6)

    def test_increment_games_won(self):
        """Test incrementing games won."""
        self.hist.increment_games_won("player1")
        self.assertEqual(self.hist.details["player1"]["Games_Won"], 4)

    def test_increment_games_lost(self):
        """Test incrementing games lost."""
        self.hist.increment_games_lost("player1")
        self.assertEqual(self.hist.details["player1"]["Games_Lost"], 3)

    def test_update_username(self):
        """Test updating username."""
        self.hist.update_username("player1", "Alice")
        self.assertEqual(self.hist.details["player1"]["Username"], "Alice")

    def test_get_username(self):
        """Test retrieving username."""
        username = self.hist.get_username("player1")
        self.assertEqual(username, "John")

    def test_check_highscore_updates(self):
        """Test highscore updates when new score is higher."""
        self.hist.check_highscore("player1", 60)
        self.assertEqual(self.hist.details["player1"]["Highscore"], 60)

    def test_check_highscore_no_update(self):
        """Test highscore does not update if score is lower."""
        self.hist.check_highscore("player1", 10)
        self.assertEqual(self.hist.details["player1"]["Highscore"], 50)

    def test_new_player_auto_initialization(self):
        """Ensure new players get initialized automatically."""
        self.hist.increment_games_played("new_player")
        self.assertIn("new_player", self.hist.details)
        self.assertEqual(self.hist.details["new_player"]["Games_Played"], 1)

    @patch("pickle.dump")
    def test_save_stats(self, mock_dump):
        """Test stats saving using mocked pickle.dump."""
        with patch("builtins.open", mock_open()):
            self.hist.save_stats()
            mock_dump.assert_called_once_with(self.hist.details, unittest.mock.ANY)


if __name__ == "__main__":
    unittest.main()
