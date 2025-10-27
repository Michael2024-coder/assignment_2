"""Unit tests for the Game class."""

import unittest
from unittest.mock import patch
from dice.game import Game


class TestGame(unittest.TestCase):
    """Test suite for the Game class."""

    def setUp(self) -> None:
        """Create a Game instance before each test."""
        self.game = Game()

    @patch("builtins.input", side_effect=["", "n"])
    @patch("dice.dice_hand.DiceHand.evaluate_roll")
    def test_single_turn_no_reroll(self, mock_evaluate, _) -> None:
        """Test a single turn where the player rolls and chooses not to roll again."""
        mock_evaluate.return_value = {
            "face_values": (3, 4),
            "total": 7,
            "is_pair": False,
            "is_single_one": False,
            "is_double_one": False,
            "must_reroll": False,
        }

        self.game.play_turn()
        self.assertEqual(self.game.current_player, "Player 2")
        self.assertEqual(self.game.scores["Player 1"], 7)
        self.assertEqual(self.game.turn_total, 0)

    @patch("builtins.input", side_effect=["", ""])
    @patch("dice.dice_hand.DiceHand.evaluate_roll")
    def test_double_one_resets_score(self, mock_evaluate, _) -> None:
        """Test that rolling double ones resets the player's score to zero."""
        self.game.scores["Player 1"] = 10
        mock_evaluate.return_value = {
            "face_values": (1, 1),
            "total": 2,
            "is_pair": True,
            "is_single_one": False,
            "is_double_one": True,
            "must_reroll": False,
        }

        self.game.play_turn()
        self.assertEqual(self.game.scores["Player 1"], 0)
        self.assertEqual(self.game.current_player, "Player 2")

    @patch("builtins.input", side_effect=["", "n", "", "n"])
    @patch("dice.dice_hand.DiceHand.evaluate_roll")
    def test_game_loop_winner(self, mock_evaluate, _) -> None:
        """Simulate a short game and check if the winner is correct."""
        mock_evaluate.side_effect = [
            {
                "face_values": (6, 6),
                "total": 12,
                "is_pair": True,
                "is_single_one": False,
                "is_double_one": False,
                "must_reroll": False,
            },
            {
                "face_values": (5, 2),
                "total": 7,
                "is_pair": False,
                "is_single_one": False,
                "is_double_one": False,
                "must_reroll": False,
            },
        ]

        self.game.scores["Player 1"] = 95
        self.game.scores["Player 2"] = 90

        self.game.start_game()
        winner = max(self.game.scores, key=self.game.scores.get)
        self.assertEqual(winner, "Player 1")
        self.assertGreaterEqual(self.game.scores[winner], 100)


if __name__ == "__main__":
    unittest.main()
