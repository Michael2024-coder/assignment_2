# test/test_game_basic.py
"""Unit tests for the Game class, covering PvP and PvC turns and utility methods."""

import unittest
from unittest.mock import patch, MagicMock
from dice.game import Game


class TestGameBasic(unittest.TestCase):
    """Basic unit tests for Game (PvP & PvC turns) plus utility methods."""

    def setUp(self):
        """Set up a Game instance with default players and scores."""
        self.game = Game()
        self.game.pvp = ["Player 1", "Player 2"]
        self.game.pvc = ["Player", "Jarvis AI"]
        self.game.pvp_scores = {p: 0 for p in self.game.pvp}
        self.game.pvc_scores = {p: 0 for p in self.game.pvc}

    # ---------------- PvP simple turn ----------------
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": False,
        "is_single_one": False,
        "must_reroll": False,
        "total": 5,
    })
    def test_pvp_play_simple(self, _mock_roll, _mock_input):
        """Test a simple PvP turn with no ones or rerolls."""
        self.game.current_player_pvp = "Player 1"
        self.game.pvp_play("1")
        self.assertEqual(self.game.pvp_scores["Player 1"], 5)
        self.assertEqual(self.game.current_player_pvp, "Player 2")

    # ---------------- PvP double one ----------------
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": True,
        "is_single_one": False,
        "must_reroll": False,
        "total": 0,
    })
    def test_pvp_play_double_one(self, _mock_roll, _mock_input):
        """Test that a double one in PvP resets the player's score to 0."""
        self.game.current_player_pvp = "Player 1"
        self.game.pvp_scores["Player 1"] = 10
        self.game.pvp_play("1")
        self.assertEqual(self.game.pvp_scores["Player 1"], 0)

    # ---------------- PvP single one ----------------
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": False,
        "is_single_one": True,
        "must_reroll": False,
        "total": 10,
    })
    def test_pvp_play_single_one(self, _mock_roll, _mock_input):
        """Test that a single one in PvP does not add to the player's score."""
        self.game.current_player_pvp = "Player 1"
        self.game.pvp_scores["Player 1"] = 15
        self.game.pvp_play("1")
        self.assertEqual(self.game.pvp_scores["Player 1"], 15)

    # ---------------- PvC simple turn ----------------
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": False,
        "is_single_one": False,
        "must_reroll": False,
        "total": 4,
    })
    def test_pvc_play_player_turn(self, _mock_roll, _mock_input):
        """Test a simple player turn in PvC mode."""
        self.game.current_player_pvc = "Player"
        self.game.pvc_play("2", "1")
        self.assertEqual(self.game.pvc_scores["Player"], 4)
        self.assertEqual(self.game.current_player_pvc, "Jarvis AI")

    # ---------------- PvC AI turn ----------------
    @patch("dice.game.Game.computer_roll")
    @patch("dice.intelligence.Intelligence.easy", return_value="n")
    def test_pvc_play_ai_turn(self, _mock_easy, mock_comp_roll):
        """Test AI turn in PvC mode."""
        self.game.current_player_pvc = "Jarvis AI"
        mock_comp_roll.return_value = {
            "is_double_one": False,
            "is_single_one": False,
            "must_reroll": False,
            "total": 7,
        }
        self.game.pvc_play("2", "1")
        self.assertEqual(self.game.pvc_scores["Jarvis AI"], 7)

    # ---------------- PvC single one ----------------
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": False,
        "is_single_one": True,
        "must_reroll": False,
        "total": 0,
    })
    def test_pvc_play_single_one_player(self, _mock_roll, _mock_input):
        """Test that a single one on the player turn in PvC does not add score."""
        self.game.current_player_pvc = "Player"
        self.game.pvc_play("2", "1")
        self.assertEqual(self.game.pvc_scores["Player"], 0)

    # ---------------- PvC double one (AI turn) ----------------
    @patch("dice.game.Game.computer_roll")
    @patch("dice.intelligence.Intelligence.easy", return_value="n")
    def test_pvc_play_double_one_ai(self, _mock_easy, mock_comp_roll):
        """Test that a double one in AI PvC turn resets the score to 0."""
        self.game.current_player_pvc = "Jarvis AI"
        mock_comp_roll.return_value = {
            "is_double_one": True,
            "is_single_one": False,
            "must_reroll": False,
            "total": 12,
        }
        self.game.pvc_scores["Jarvis AI"] = 20
        self.game.pvc_play("2", "1")
        self.assertEqual(self.game.pvc_scores["Jarvis AI"], 0)

    # ---------------- PvC must reroll ----------------
    @patch("builtins.input", side_effect=["n", "n"])
    @patch("dice.game.Game.roll", side_effect=[
        {
            "is_double_one": False, "is_single_one": False,
            "must_reroll": True, "total": 6
            },
        {
            "is_double_one": False, "is_single_one": False,
            "must_reroll": False, "total": 4
            },
    ])
    def test_pvc_play_must_reroll(self, _mock_roll, _mock_input):
        """Test that a reroll in PvC adds to the turn total correctly."""
        self.game.current_player_pvc = "Player"
        self.game.pvc_scores["Player"] = 0
        self.game.pvc_play("2", "1")
        self.assertEqual(self.game.pvc_scores["Player"], 10)

    # ---------------- PvP pause/quit ----------------
    @patch("builtins.input", side_effect=["p", "4", "y"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": False,
        "is_single_one": False,
        "must_reroll": False,
        "total": 8,
    })
    def test_pvp_pause_quit(self, _mock_roll, _mock_input):
        """Test pausing then quitting during PvP returns 'quit' and resets score."""
        self.game.current_player_pvp = "Player 1"
        result = self.game.pvp_play("1")
        self.assertEqual(result, "quit")
        self.assertEqual(self.game.pvp_scores["Player 1"], 0)
        self.assertEqual(self.game.turn_total, 0)

    # ---------------- PvC player changes name ----------------
    @patch("builtins.input", side_effect=["p", "3", "player123", "NewName", "n"])
    @patch("dice.game.Game.roll", return_value={
        "is_double_one": False,
        "is_single_one": False,
        "must_reroll": False,
        "total": 5,
    })
    def test_pvc_player_change_name(self, _mock_roll, _mock_input):
        """Test updating the PvC player's name mid-turn."""
        self.game.current_player_pvc = "Player"
        self.game.pvc_scores["Player"] = 0
        self.game.pvc_play("2", "1")
        self.assertIn("NewName", self.game.pvc)
        self.assertEqual(self.game.current_player_pvc, "Jarvis AI")
        self.assertEqual(self.game.pvc_scores["NewName"], 5)

    # ---------------- PvC AI mid hold ----------------
    @patch("dice.game.Game.computer_roll")
    @patch("dice.intelligence.Intelligence.mid", return_value="n")
    def test_pvc_ai_mid_hold(self, _mock_mid, mock_comp_roll):
        """Test medium-level AI deciding to hold in PvC."""
        self.game.current_player_pvc = "Jarvis AI"
        self.game.pvc_scores["Jarvis AI"] = 10
        mock_comp_roll.return_value = {
            "is_double_one": False,
            "is_single_one": False,
            "must_reroll": False,
            "total": 15,
        }
        self.game.pvc_play("2", "2")
        self.assertEqual(self.game.pvc_scores["Jarvis AI"], 25)
        self.assertEqual(self.game.current_player_pvc, "Player")

    # ---------------- Switch PvP ----------------
    def test_switch_pvp(self):
        """Test switching turn in PvP resets turn total."""
        self.game.turn_total = 12
        self.game.current_player_pvp = "Player 1"
        self.game.switch_pvp()
        self.assertEqual(self.game.current_player_pvp, "Player 2")
        self.assertEqual(self.game.turn_total, 0)

    # ---------------- Switch PvC ----------------
    def test_switch_pvc(self):
        """Test switching turn in PvC resets turn total."""
        self.game.turn_total = 15
        self.game.current_player_pvc = "Player"
        self.game.switch_pvc()
        self.assertEqual(self.game.current_player_pvc, "Jarvis AI")
        self.assertEqual(self.game.turn_total, 0)

    # ---------------- Double one PvP ----------------
    def test_double_one_pvp_resets_score(self):
        """Test double one in PvP resets player's score."""
        self.game.current_player_pvp = "Player 1"
        self.game.pvp_scores["Player 1"] = 50
        self.game.double_one_pvp()
        self.assertEqual(self.game.pvp_scores["Player 1"], 0)

    # ---------------- Double one PvC ----------------
    def test_double_one_pvc_resets_score(self):
        """Test double one in PvC resets player's score."""
        self.game.current_player_pvc = "Player"
        self.game.pvc_scores["Player"] = 40
        self.game.double_one_pvc()
        self.assertEqual(self.game.pvc_scores["Player"], 0)

    # ---------------- Save PvP1 stats ----------------
    def test_save_pvp1_updates_stats(self):
        """Test saving PvP1 stats updates histogram + highscore."""
        self.game.pvp_scores = {"Player 1": 50, "Player 2": 40}
        self.game.histogram = MagicMock()
        self.game.highscore = MagicMock()
        self.game.save_pvp1("p1_id", "Player 1")
        self.game.histogram.increment_games_played.assert_called_with("p1_id")
        self.game.histogram.increment_games_won.assert_called_with("p1_id")
        self.game.highscore.set_highscore.assert_called_with(50)
        self.game.histogram.check_highscore.assert_called()

    # ---------------- Save PvC1 player wins ----------------
    def test_save_pvc1_player_wins(self):
        """Test saving PvC stats when player wins updates histogram & highscore."""
        self.game.pvc_scores = {"Player": 60, "Jarvis AI": 45}
        self.game.histogram = MagicMock()
        self.game.highscore = MagicMock()
        self.game.save_pvc1("user123", "Player")
        self.game.histogram.increment_games_played.assert_called_with("user123")
        self.game.histogram.increment_games_won.assert_called_with("user123")
        self.game.highscore.set_highscore.assert_called_with(60)

    # ---------------- player_type new ----------------
    @patch("builtins.input", side_effect=["1", "newID123", "NewPlayer"])
    def test_player_type_new(self, _mock_input):
        """Test player_type when creating a new player."""
        self.game.player = MagicMock()
        self.game.histogram = MagicMock()
        self.game.player.get_user_id_list.return_value = []
        self.game.player.get_user_id.return_value = "newID123"
        self.game.player.get_username.return_value = "NewPlayer"
        user_id, username = self.game.player_type()
        self.assertEqual(user_id, "newID123")
        self.assertEqual(username, "NewPlayer")

    # ---------------- player_type existing ----------------
    @patch("builtins.input", side_effect=["2", "existingID"])
    def test_player_type_existing(self, _mock_input):
        """Test player_type when selecting an existing player."""
        self.game.player = MagicMock()
        self.game.histogram = MagicMock()
        self.game.player.get_user_id_list.return_value = ["existingID"]
        self.game.player.get_user_id.return_value = "existingID"
        self.game.histogram.get_username = MagicMock(return_value="ExistingPlayer")
        user_id, username = self.game.player_type()
        self.assertEqual(user_id, "existingID")
        self.assertEqual(username, "ExistingPlayer")


if __name__ == "__main__":
    unittest.main()
