"""Player module for managing individual game participants and their statistics."""
import pickle


class Player:
    """
    Represents a player in the game, tracking identity.

    score, and game statistics.
    """

    def __init__(self):  # pragma: no cover
        """
        Initialize a new Player instance with a unique ID and username.

        Attributes:
            __username (str): The player's username.
            __userid (str): The player's unique ID.
            user_id_list (list): List of all existing user IDs.
        """
        self.__username = ""
        self.__userid = ""
        self.user_id_list = self.get_user_id_list()

    def set_id(self, p_id: str) -> None:  # pragma: no cover
        """
        Set the player's unique ID and add it to the persistent ID list if new.

        Args:
            id (str): The unique identifier to assign to the player.
        """
        self.__userid = p_id
        if self.__userid not in self.user_id_list:
            self.user_id_list.add(self.__userid)
            with open('dice\\user_id.ser', 'wb') as ids:
                pickle.dump(self.user_id_list, ids)

    def set_username(self, name: str) -> None:  # pragma: no cover
        """
        Set the player's username directly (without validation).

        Args:
            name (str): The new username.
        """
        self.__username = name

    def get_user_id_list(self) -> list:  # pragma: no cover
        """
        Retrieve the list of all existing player IDs from persistent storage.

        Returns:
            list: A list of existing user IDs.
        """
        try:
            with open('dice\\user_id.ser', 'rb') as ids:
                user_id_list = pickle.load(ids)
            return user_id_list
        except FileNotFoundError:
            return {}

    def get_user_id(self) -> str:  # pragma: no cover
        """
        Get the player's unique ID.

        Returns:
            str: The player's user ID.
        """
        return self.__userid

    def get_username(self) -> str:  # pragma: no cover
        """
        Retrieve the player's current username.

        Returns:
            str: The player's username.
        """
        return self.__username
