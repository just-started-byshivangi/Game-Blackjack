class Card:
    
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
    
    
    def __str__(self):
        return self.ranks + " of "+ self.suits 