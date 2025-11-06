
class Intelligence:
    def __init__(self):
        self.medium_turn_count = 5
        self.score_list = []
        
    def easy_level(self, turn_total):
        if turn_total >= 20:
            return 'n'
        else:
            return 'y'
        
    def medium_level(self, turn_total, score, comp_double_one):
        if score not in self.score_list:
            self.medium_turn_count-=1
            self.score_list.append(score)
        
        if comp_double_one:
            self.medium_turn_count = 5
            self.score_list = []
            
        if self.medium_turn_count > 0 and  self.medium_turn_count < 4:
            remainder = int((100-score)/self.medium_turn_count)
            if turn_total >= remainder:
                return 'n'
            else:
                return 'y'
            
        elif self.medium_turn_count == 4:
            if turn_total >= 25:
                return 'n'
            else:
                return 'y'
        
            
        
    def hard_level(self, turn_total, player_score, computer_score):
        if player_score >= 71 or computer_score >= 71:
            if turn_total >= 100-computer_score:
                return 'n'
            else:
                return 'y'
        else:
            score_diff = 0
            if player_score > computer_score:
                score_diff = player_score - computer_score
            elif computer_score > player_score:
                score_diff = computer_score - player_score
                
            if turn_total >= int(21 + ((score_diff)/8)):
                return 'n'
            else:
                return 'y'