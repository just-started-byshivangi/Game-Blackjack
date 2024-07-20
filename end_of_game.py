def player_busts(player,dealer,chips):
    print("Player loses")
    chips.lose_bet()
    pass

def player_wins(player,dealer,chips):
    print("Player Wins!!")
    chips.win_bet()
    pass

def dealer_busts(player,dealer,chips):
    print("Dealer loses")
    chips.lose_bet()
    pass
    
def dealer_wins(player,dealer,chips):
    print("Dealer Wins!!")
    chips.win_bet()
    pass
    
def push(player,dealer):
    print("Its a tie between the player and the dealer!! its a push!!")
    pass