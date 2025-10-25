class Player:
    """
    Represents a player in the game, tracking identity, score, and game statistics.
    """

    ids = 0  # Class-level counter to assign unique IDs to each player

    def __init__(self, username: str):
        """
        Initialize a new Player instance with a unique ID and username.

        Args:
            username (str): The player's chosen username.
        """
        Player.ids += 1
        self.id = Player.ids
        self.__username = username
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.current_score = 0

    def change_username(self, new_name: str):
        """
        Change the player's username after validating the new name.

        Args:
            new_name (str): The new username to assign.

        Raises:
            ValueError: If the new name does not contain at least one
                alphabetic character.
        """
        new_name = new_name.strip()
        if not any(char.isalpha() for char in new_name):
            raise ValueError(
                "Invalid name! Username must contain at least one letter."
            )
        old_name = self.__username
        self.__username = new_name
        print(
            f"Username changed from '{old_name}' to '{new_name}'"
        )

    def set_username(self, name: str):
        """
        Set the player's username directly (without validation).

        Args:
            name (str): The new username.
        """
        self.__username = name

    def get_username(self) -> str:
        """
        Retrieve the player's current username.

        Returns:
            str: The player's username.
        """
        return self.__username

    def reset_score(self):
        """
        Reset the player's current score to zero.
        """
        self.current_score = 0

    def increment_games_played(self):
        """
        Increment the count of games the player has played.
        """
        self.games_played += 1

    def increment_games_won(self):
        """
        Increment the count of games the player has won.
        """
        self.games_won += 1

    def increment_games_lost(self):
        """
        Increment the count of games the player has lost.
        """
        self.games_lost += 1

    def get_stats(self) -> dict:
        """
        Retrieve a dictionary of the player's current statistics.

        Returns:
            dict: A dictionary containing the player's ID,
            username, score, and game stats.
        """
        return {
            "id": self.id,
            "username": self.__username,
            "score": self.current_score,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "games_lost": self.games_lost,
        }

    def __str__(self) -> str:
        """
        Return a string representation of the player.

        Returns:
            str: A formatted string with the player's ID,
            username, and score.
        """
        return (
            f"ID: {self.id} | Username: {self.__username} | "
            f"Score: {self.current_score}"
        )
