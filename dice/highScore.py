# 

# dice/HighScore.py

import pickle
from dice.Player import Player


class HighScore:
    def __init__(self):
        self.players = {}

    def add_player(self, player: Player):
        if player.id in self.players:
            return "Player already exists!"
        self.players[player.id] = player
        return "Player added successfully."

    def update_score(self, player_id, point):
        if point < 0:
            raise ValueError("Score cannot be negative")
        if player_id in self.players:
            self.players[player_id].current_score += point
        else:
            raise KeyError("Player not found")

    def reset_score(self, player_id):
        if player_id in self.players:
            self.players[player_id].reset_score()
        else:
            raise KeyError("Player not found")

    def increment_stat(self, player_id, stat_type):
        if player_id not in self.players:
            raise KeyError("Player not found")
        if stat_type == "games_played":
            self.players[player_id].games_played += 1
        else:
            raise ValueError("Invalid stat type")

    def get_player_stats(self, player_id):
        if player_id in self.players:
            return self.players[player_id].get_stats()
        raise KeyError("Player not found")

    def get_leaderboard(self, top_n=10):
        sorted_players = sorted(
            self.players.values(),
            key=lambda p: p.current_score,
            reverse=True
        )
        return [(p.get_username(), p.current_score) for p in sorted_players[:top_n]]

    def change_username(self, player_id, new_name):
        if player_id in self.players:
            self.players[player_id].change_username(new_name)
        else:
            raise KeyError("Player not found")

    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.players, f)

    def load_from_file(self, filename):
        with open(filename, "rb") as f:
            self.players = pickle.load(f)

    def get_total_score(self, player_id):
        if player_id in self.players:
            return self.players[player_id].current_score
        raise KeyError("Player not found")
