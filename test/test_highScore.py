import unittest
import os
from dice.Player import Player
from dice.highScore import HighScore


class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.hs = HighScore()
        self.p1 = Player("Michael")
        self.p2 = Player("Ngozi")
        self.hs.add_player(self.p1)
        self.hs.add_player(self.p2)

    def test_add_existing_player(self):
        result = self.hs.add_player(self.p1)
        self.assertEqual(result, "Player already exists!")

    def test_update_score_valid(self):
        self.hs.update_score(self.p1.id, 30)
        self.assertEqual(self.p1.current_score, 30)

    def test_update_score_invalid(self):
        with self.assertRaises(ValueError):
            self.hs.update_score(self.p1.id, -10)

    def test_reset_score(self):
        self.p2.current_score = 50
        self.hs.reset_score(self.p2.id)
        self.assertEqual(self.p2.current_score, 0)

    def test_increment_stat_valid(self):
        self.hs.increment_stat(self.p1.id, "games_played")
        self.assertEqual(self.p1.games_played, 1)

    def test_increment_stat_invalid(self):
        with self.assertRaises(ValueError):
            self.hs.increment_stat(self.p1.id, "invalid_stat")

    def test_get_player_stats(self):
        stats = self.hs.get_player_stats(self.p2.id)
        self.assertEqual(stats["score"], 0)
        self.assertEqual(stats["games_played"], 0)

    def test_get_leaderboard(self):
        self.hs.update_score(self.p1.id, 100)
        self.hs.update_score(self.p2.id, 50)
        leaderboard = self.hs.get_leaderboard()
        self.assertEqual(leaderboard[0][0], "Michael")

    def test_change_username_valid(self):
        self.hs.change_username(self.p2.id, "Big Mike")
        self.assertEqual(self.p2.get_username(), "Big Mike")

    def test_change_username_invalid(self):
        with self.assertRaises(ValueError):
            self.hs.change_username(self.p1.id, "123")

    def test_save_and_load(self):
        filename = "test_highscore.pkl"
        self.hs.update_score(self.p1.id, 40)
        self.hs.save_to_file(filename)

        new_hs = HighScore()
        new_hs.load_from_file(filename)
        self.assertEqual(new_hs.get_total_score(self.p1.id), 40)

        os.remove(filename)

    def test_get_total_score(self):
        self.hs.update_score(self.p2.id, 25)
        score = self.hs.get_total_score(self.p2.id)
        self.assertEqual(score, 25)


if __name__ == "__main__":
    unittest.main()