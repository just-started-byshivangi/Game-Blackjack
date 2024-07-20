def show_all(player,dealer):
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print(f"Dealers value if :{dealer.value}")   

    
    print("Player's Hand:")
    for card in player.cards:
        print(card)
    print(f"Player value if :{player.value}")