"""
Unit tests for the Game class.
"""

import unittest
from unittest.mock import patch
from dice.game import Game


class TestGame(unittest.TestCase):
    """Test suite for the Game controller."""

    def setUp(self):
        """Create a fresh Game instance for each test."""
        self.game = Game()
        # Initialize scores to avoid KeyErrors
        self.game.pvp_scores = {player: 0 for player in self.game.pvp}
        self.game.pvc_scores = {player: 0 for player in self.game.pvc}

    def test_switch_pvp(self):
        """Test switching between PvP players."""
        self.game.current_player_pvp = self.game.pvp[0]
        self.game.switch_pvp()
        self.assertEqual(self.game.current_player_pvp, self.game.pvp[1])
        self.assertEqual(self.game.turn_total, 0)

        self.game.switch_pvp()
        self.assertEqual(self.game.current_player_pvp, self.game.pvp[0])

    def test_switch_pvc(self):
        """Test switching between PvC participants."""
        self.game.current_player_pvc = self.game.pvc[0]
        self.game.switch_pvc()
        self.assertEqual(self.game.current_player_pvc, self.game.pvc[1])
        self.assertEqual(self.game.turn_total, 0)

        self.game.switch_pvc()
        self.assertEqual(self.game.current_player_pvc, self.game.pvc[0])

    @patch("builtins.input", return_value="1")
    @patch("sys.stdout")
    def test_game_mode(self, _mock_stdout, _mock_input):
        """Test game_mode input returns the selected option."""
        choice = self.game.game_mode()
        self.assertEqual(choice, "1")

    @patch("builtins.input", return_value="2")
    @patch("sys.stdout")
    def test_game_level(self, _mock_stdout, _mock_input):
        """Test game_level input returns the selected level."""
        choice = self.game.game_level()
        self.assertEqual(choice, "2")

    def test_add_turn_total(self):
        """Test adding dice roll results to turn total."""
        self.game.turn_total = 0
        self.game.add_turn_total({"total": 7})
        self.assertEqual(self.game.turn_total, 7)
        self.game.add_turn_total({"total": 3})
        self.assertEqual(self.game.turn_total, 10)

    def test_double_one_pvp_and_pvc(self):
        """Test that double_one resets the score in PvP and PvC."""
        self.game.current_player_pvp = self.game.pvp[0]
        self.game.pvp_scores[self.game.current_player_pvp] = 50
        self.game.double_one_pvp()
        self.assertEqual(self.game.pvp_scores[self.game.current_player_pvp], 0)

        self.game.current_player_pvc = self.game.pvc[0]
        self.game.pvc_scores[self.game.current_player_pvc] = 40
        self.game.double_one_pvc()
        self.assertEqual(self.game.pvc_scores[self.game.current_player_pvc], 0)

    @patch("dice.dice_hand.DiceHand.evaluate_roll", return_value={
        "total": 5,
        "is_double_one": False,
        "is_single_one": False,
        "must_reroll": False
    })
    @patch("dice.dice_hand.DiceHand.display_dice", return_value="dice faces")
    @patch("builtins.input", return_value="")
    @patch("sys.stdout")
    def test_roll_and_computer_roll(
        self,
        _mock_stdout,
        _mock_input,
        _mock_display,
        _mock_eval
    ):
        """Test rolling dice for player and AI."""
        result = self.game.roll()
        self.assertEqual(result["total"], 5)

        result_ai = self.game.computer_roll()
        self.assertEqual(result_ai["total"], 5)

    @patch("sys.stdout")
    def test_scoreboard(self, _mock_stdout):
        """Test that scoreboard prints correctly."""
        self.game.pvp_scores = {self.game.pvp[0]: 10, self.game.pvp[1]: 20}
        self.game.pvc_scores = {self.game.pvc[0]: 15, self.game.pvc[1]: 25}

        # PvP scoreboard
        self.game.scoreboard("1")
        # PvC scoreboard
        self.game.scoreboard("2")


if __name__ == "__main__":
    unittest.main()
