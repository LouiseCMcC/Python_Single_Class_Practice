

class Team:
    
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)
        
    def has_player(self, name):
        for player in self.players:
            if player == name:
                return True
        else:
            return False
    
    def play_game(self, win):
        if win == True:
            self.points += 3
    
    