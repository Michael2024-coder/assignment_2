"""
Histogram module for tracking and managing player gameplay statistics.

This module provides the `Histogram` class, which handles:
- Keeping records for each player (username, highscore, wins, losses, games played)
- Updating statistics after each game event
- Loading statistics from a serialized file on startup
- Saving updated statistics back to the file

The statistics are stored in a dictionary keyed by player ID, and
persisted using Python's `pickle` module.
"""

import pickle


class Histogram:
    """
    Manages player statistics such as wins, losses.

    Including games played, high scores, and usernames..

    Handles loading and saving these statistics to a serialized file.
    """

    def __init__(self):  # pragma: no cover
        """
        Initialize the Histogram by loading existing player statistics.

        From the stats file.
        """
        self.details = self.load_stats_file()

    def increment_games_played(self, p_id: str) -> None:  # pragma: no cover
        """
        Increment the count of games the player has played.

        Args:
            id (str): The player's unique identifier.
        """
        if p_id not in self.details.keys():
            self.details[p_id] = {
                                    "Username": "",
                                    "Highscore": 0,
                                    "Games_Played": 0,
                                    "Games_Won": 0,
                                    "Games_Lost": 0
                                }
        games_played_value = self.details[p_id].get("Games_Played", 0)
        self.details[p_id]["Games_Played"] = games_played_value + 1

    def increment_games_won(self, p_id: str) -> None:  # pragma: no cover
        """
        Increment the count of games the player has won.

        Args:
            id (str): The player's unique identifier.
        """
        if p_id not in self.details.keys():
            self.details[p_id] = {
                                    "Username": "",
                                    "Highscore": 0,
                                    "Games_Played": 0,
                                    "Games_Won": 0,
                                    "Games_Lost": 0
                                }
        games_won_value = self.details[p_id].get("Games_Won", 0)
        self.details[p_id]["Games_Won"] = games_won_value + 1

    def increment_games_lost(self, p_id: str) -> None:  # pragma: no cover
        """
        Increment the count of games the player has lost.

        Args:
            id (str): The player's unique identifier.
        """
        if p_id not in self.details.keys():
            self.details[p_id] = {
                                    "Username": "",
                                    "Highscore": 0,
                                    "Games_Played": 0,
                                    "Games_Won": 0,
                                    "Games_Lost": 0
                                }
        games_lost_value = self.details[p_id].get("Games_Lost", 0)
        self.details[p_id]["Games_Lost"] = games_lost_value + 1

    def update_username(self, p_id: str, name: str) -> None:  # pragma: no cover
        """
        Update or set the username associated with the given player ID.

        Args:
            id (str): The player's unique identifier.
            name (str): The username to assign.
        """
        if p_id not in self.details.keys():
            self.details[p_id] = {
                                    "Username": "",
                                    "Highscore": 0,
                                    "Games_Played": 0,
                                    "Games_Won": 0,
                                    "Games_Lost": 0
                                }
        self.details[p_id]["Username"] = name

    def get_username(self, p_id: str) -> str:  # pragma: no cover
        """
        Retrieve the username associated with the given player ID.

        Args:
            id (str): The player's unique identifier.

        Returns:
            str: The stored username.
        """
        return self.details[p_id]["Username"]

    def check_highscore(self, p_id: str, score: int) -> None:  # pragma: no cover
        """
        Update the player's high score if the provided score is higher.

        Than the current recorded high score.

        Args:
            id (str): The player's unique identifier.
            score (int): The new score to evaluate.
        """
        if p_id not in self.details.keys():
            self.details[p_id] = {
                                    "Username": "",
                                    "Highscore": 0,
                                    "Games_Played": 0,
                                    "Games_Won": 0,
                                    "Games_Lost": 0
                                }
        if score > self.details[p_id]["Highscore"]:
            self.details[p_id]["Highscore"] = score

    def save_stats(self) -> None:  # pragma: no cover
        """Save all current player statistics to the serialized stats file."""
        with open("dice\\history.ser", "wb") as f:
            pickle.dump(self.details, f)

    def load_stats_file(self) -> dict:  # pragma: no cover
        """
        Load and return player statistics from the serialized stats file.

        Returns:
            dict: A dictionary containing all stored player statistics.
        """
        with open("dice\\history.ser", "rb") as f:
            details = pickle.load(f)
        return details
