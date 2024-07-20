def show_some(player,dealer):
    print("Dealer's Hand:")
    print("  <card hidden>   ")
    print(dealer.cards[1])

    print("Player's Hand:")
    for card in player.cards:
        print(card)