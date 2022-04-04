#write class here

class Team:
    def __init__ (self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0 #not passed in the constructor because you don't know what the value is goint to be
    
    def add_player(self,new_player):
        self.players.append(new_player)

    #instructors solution to below:
    #return self.players.count(player)>0
    #count if the argument Junior Bevil is in the list
    #and if the count is greater than 0 return True or False
    
    def has_player(self, player_there):
        for player in self.players:
            if player == player_there:
                return True
            
        return False

    def play_game(self, has_won):
        if has_won == True:     # == True is redundant because has_won is either Trues or false
            self.points += 3





    


