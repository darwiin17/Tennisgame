#Skapar attribut till objektet player
class player:
    def __init__(self, name, chance, wins, played):
            self.name = name
            self.chance = chance
            self.wins = wins
            self.played = played
    def won_game(self):
            self.wins = self.wins + 1
            self.played = self.played + 1
    def loose_game(self):
        	self.played = self.played + 1
