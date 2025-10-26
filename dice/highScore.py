"""HighScore module for managing player scores and stats."""

import pickle
from dice.player import Player


class HighScore:
    """Tracks players, scores, and game statistics."""

    def __init__(self):
        """Initialize an empty dictionary of players."""
        self.players = {}

    def add_player(self, player: Player) -> str:
        """
        Add a new player to the system.

        Args:
            player (Player): The player object to add.

        Returns:
            str: Success or failure message.
        """
        if player.id in self.players:
            return "Player already exists!"
        self.players[player.id] = player
        return "Player added successfully."

    def update_score(self, player_id: str, point: int) -> None:
        """
        Update a player's score.

        Args:
            player_id (str): Unique player ID.
            point (int): Points to add.

        Raises:
            ValueError: If point is negative.
            KeyError: If player ID is not found.
        """
        if point < 0:
            raise ValueError("Score cannot be negative")
        if player_id not in self.players:
            raise KeyError("Player not found")
        self.players[player_id].current_score += point

    def reset_score(self, player_id: str) -> None:
        """
        Reset a player's score to zero.

        Args:
            player_id (str): Unique player ID.

        Raises:
            KeyError: If player ID is not found.
        """
        if player_id not in self.players:
            raise KeyError("Player not found")
        self.players[player_id].reset_score()

    def increment_stat(self, player_id: str, stat_type: str) -> None:
        """
        Increment a player's stat.

        Args:
            player_id (str): Unique player ID.
            stat_type (str): Stat to increment (e.g., 'games_played').

        Raises:
            KeyError: If player ID is not found.
            ValueError: If stat_type is invalid.
        """
        if player_id not in self.players:
            raise KeyError("Player not found")
        if stat_type == "games_played":
            self.players[player_id].games_played += 1
        else:
            raise ValueError("Invalid stat type")

    def get_player_stats(self, player_id: str) -> dict:
        """
        Get a player's statistics.

        Args:
            player_id (str): Unique player ID.

        Returns:
            dict: Player stats.

        Raises:
            KeyError: If player ID is not found.
        """
        if player_id not in self.players:
            raise KeyError("Player not found")
        return self.players[player_id].get_stats()

    def get_leaderboard(self, top_n: int = 10) -> list:
        """
        Get the top N players by score.

        Args:
            top_n (int): Number of top players to return.

        Returns:
            list: List of (username, score) tuples.
        """
        sorted_players = sorted(
            self.players.values(),
            key=lambda p: p.current_score,
            reverse=True
        )
        return [(p.get_username(), p.current_score) for p in sorted_players[:top_n]]

    def change_username(self, player_id: str, new_name: str) -> None:
        """
        Change a player's username.

        Args:
            player_id (str): Unique player ID.
            new_name (str): New username.

        Raises:
            KeyError: If player ID is not found.
            ValueError: If new_name is invalid.
        """
        if player_id not in self.players:
            raise KeyError("Player not found")
        self.players[player_id].change_username(new_name)

    def save_to_file(self, filename: str) -> None:
        """
        Save all player data to a file.

        Args:
            filename (str): File path to save data.
        """
        with open(filename, "wb") as f:
            pickle.dump(self.players, f)

    def load_from_file(self, filename: str) -> None:
        """
        Load player data from a file.

        Args:
            filename (str): File path to load data from.
        """
        with open(filename, "rb") as f:
            self.players = pickle.load(f)

    def get_total_score(self, player_id: str) -> int:
        """
        Get a player's total score.

        Args:
            player_id (str): Unique player ID.

        Returns:
            int: Player's current score.

        Raises:
            KeyError: If player ID is not found.
        """
        if player_id not in self.players:
            raise KeyError("Player not found")
        return self.players[player_id].current_score
