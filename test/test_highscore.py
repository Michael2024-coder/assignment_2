"""Unit tests for the HighScore class and its integration with Player."""

import unittest
import os
from dice.player import Player
from dice.highscore import HighScore


class TestHighScore(unittest.TestCase):
    """Test suite for verifying HighScore functionality."""

    def setUp(self):
        """Initialize test environment with two sample players."""
        self.hs = HighScore()
        self.p1 = Player("Michael")
        self.p2 = Player("Ngozi")
        self.hs.add_player(self.p1)
        self.hs.add_player(self.p2)

    def test_add_existing_player(self):
        """Test that adding an existing player returns a warning message."""
        result = self.hs.add_player(self.p1)
        self.assertEqual(result, "Player already exists!")

    def test_update_score_valid(self):
        """Test that score updates correctly with valid input."""
        self.hs.update_score(self.p1.id, 30)
        self.assertEqual(self.p1.current_score, 30)

    def test_update_score_invalid(self):
        """Test that negative score raises ValueError."""
        with self.assertRaises(ValueError):
            self.hs.update_score(self.p1.id, -10)

    def test_reset_score(self):
        """Test that reset_score sets player's score to zero."""
        self.p2.current_score = 50
        self.hs.reset_score(self.p2.id)
        self.assertEqual(self.p2.current_score, 0)

    def test_increment_stat_valid(self):
        """Test that games_played stat increments correctly."""
        self.hs.increment_stat(self.p1.id, "games_played")
        self.assertEqual(self.p1.games_played, 1)

    def test_increment_stat_invalid(self):
        """Test that invalid stat type raises ValueError."""
        with self.assertRaises(ValueError):
            self.hs.increment_stat(self.p1.id, "invalid_stat")

    def test_get_player_stats(self):
        """Test that get_player_stats returns correct initial values."""
        stats = self.hs.get_player_stats(self.p2.id)
        self.assertEqual(stats["score"], 0)
        self.assertEqual(stats["games_played"], 0)

    def test_get_leaderboard(self):
        """Test that leaderboard returns players sorted by score."""
        self.hs.update_score(self.p1.id, 100)
        self.hs.update_score(self.p2.id, 50)
        leaderboard = self.hs.get_leaderboard()
        self.assertEqual(leaderboard[0][0], "Michael")

    def test_change_username_valid(self):
        """Test that change_username updates the player's name."""
        self.hs.change_username(self.p2.id, "Big Mike")
        self.assertEqual(self.p2.get_username(), "Big Mike")

    def test_change_username_invalid(self):
        """Test that invalid username raises ValueError."""
        with self.assertRaises(ValueError):
            self.hs.change_username(self.p1.id, "123")

    def test_save_and_load(self):
        """Test saving and loading player data using pickle."""
        filename = "test_highscore.pkl"
        self.hs.update_score(self.p1.id, 40)
        self.hs.save_to_file(filename)

        new_hs = HighScore()
        new_hs.load_from_file(filename)
        self.assertEqual(new_hs.get_total_score(self.p1.id), 40)

        os.remove(filename)

    def test_get_total_score(self):
        """Test that get_total_score returns correct value."""
        self.hs.update_score(self.p2.id, 25)
        score = self.hs.get_total_score(self.p2.id)
        self.assertEqual(score, 25)


if __name__ == "__main__":
    unittest.main()
