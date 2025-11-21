"""
Unit tests for the Main class of the Two-Dice Pig game.

Tests menu display, rules display, statistics display, and play flow.
Uses minimal mocks to isolate external dependencies.
"""

import unittest
from unittest.mock import patch, mock_open
from io import StringIO

from dice.main import Main


class TestMain(unittest.TestCase):
    """Test suite for the Main application controller."""

    @patch("dice.histogram.Histogram.load_stats_file", return_value={})
    @patch("dice.player.Player.get_user_id_list", return_value=[])
    @patch("builtins.input", return_value="2")
    @patch("sys.stdout", new_callable=StringIO)
    def test_menu(self, mock_stdout, _mock_input, _mock_uids, _mock_stats):
        """Test that the menu method returns the user choice and prints the menu."""
        main = Main()
        choice = main.menu()

        self.assertEqual(choice, "2")
        self.assertIn("Main Menu", mock_stdout.getvalue())
        self.assertIn("1. Play Game", mock_stdout.getvalue())

    @patch("dice.histogram.Histogram.load_stats_file", return_value={})
    @patch("dice.player.Player.get_user_id_list", return_value=[])
    @patch("builtins.open", new_callable=mock_open, read_data="Game rules content")
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_rules(self, mock_stdout, mock_file, _mock_uids, _mock_stats):
        """Test that display_rules prints the welcome message and rules content."""
        main = Main()
        main.display_rules()

        output = mock_stdout.getvalue()
        self.assertIn("Welcome to Two-Dice Pig", output)
        self.assertIn("Game rules content", output)
        mock_file.assert_called_once_with('dice\\rules.txt', 'r', encoding='utf-8')

    @patch(
        "dice.histogram.Histogram.load_stats_file",
        return_value={
            "player1": {
                "username": "Alice",
                "highscore": 50,
                "games_played": 10,
                "games_won": 6,
                "games_lost": 4
            }
        }
    )
    @patch("dice.player.Player.get_user_id_list", return_value=[])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_stats(self, mock_stdout, _mock_uids, _mock_stats):
        """Test that display_stats prints the correct player statistics."""
        main = Main()
        main.display_stats()

        output = mock_stdout.getvalue()
        self.assertIn("Username: Alice", output)
        self.assertIn("Highscore: 50", output)
        self.assertIn("Games Played: 10", output)
        self.assertIn("Games Won: 6", output)
        self.assertIn("Games Lost: 4", output)

    @patch("dice.histogram.Histogram.load_stats_file", return_value={})
    @patch("dice.player.Player.get_user_id_list", return_value=[])
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input")
    def test_play_flow(self, mock_input, _mock_stdout, _mock_uids, _mock_stats):
        """
        Test the play method flow:
        Press Enter after rules, choose option 1 to start game, then choose 3 to quit.
        """
        mock_input.side_effect = ["", "1", "3"]

        main = Main()

        # Patch start_game to prevent running full game logic
        with patch.object(main.game, "start_game") as fake_start:
            # Patch display_rules to prevent printing long text
            with patch.object(main, "display_rules"):
                main.play()
                fake_start.assert_called_once()

        # Ensure the input sequence was followed
        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()
