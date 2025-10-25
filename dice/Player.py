class Player:
    ids = 0
    
    def __init__(self,username):
        Player.ids += 1
        self.id = Player.ids
        self.__username = username
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.current_score = 0
       
    def change_username(self, new_name):
        new_name = new_name.strip()
        if not any(char.isalpha() for char in new_name):
            raise ValueError("Invalid name! Username must contain at least one letter.")
        old_name = self.__username
        self.__username = new_name
        print(f"Username changed from '{old_name}' to '{new_name}'")

    def set_username(self, name): 
        self.__username = name

    def get_username(self):
        return self.__username
    
    def reset_score(self):
        self.current_score = 0

    def increment_games_played(self):
        self.games_played += 1

    def increment_games_won(self):
        self.games_won += 1

    def increment_games_lost(self):
        self.games_lost += 1

    def get_stats(self):
        return {
            "id": self.id,
            "username": self.__username,
            "score": self.current_score,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "games_lost": self.games_lost
        }

    def __str__(self):
        return f"ID: {self.id} | Username: {self.__username} | Score: {self.current_score}" 
    

