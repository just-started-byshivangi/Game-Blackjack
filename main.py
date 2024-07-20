from card import Card
from deck import Deck
from hand import Hand
from chips import Chips 
from hit_or_stand import hit_or_stand
from hit import hit
from take_bet import take_bet
from show_all import show_all
from show_some import show_some
from end_of_game import player_busts
from end_of_game import player_wins
from end_of_game import dealer_busts
from end_of_game import dealer_wins
from end_of_game import push
while True:
    # Print an opening statement
    print("Welcome to the game Blackjack!! \n\
           You have to come closer to 21 as much as you can with the help of hit and stand but more than the dealer,she can hit until 17.\n\
           Ace can be adjusted as 1 or 11.")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    Player_hand = Hand()
    Player_hand.add_card(deck.deal())
    Player_hand.add_card(deck.deal())
    
    Dealer_hand = Hand()
    Dealer_hand.add_card(deck.deal())
    Dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    Player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(Player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(Player_hand,Dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,Player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(Player_hand,Dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if Player_hand.value > 21:
            player_busts(Player_hand,Dealer_hand,Player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if Player_hand.value <= 21:
        while Dealer_hand.value < 17:
           hit(deck,Dealer_hand)
      
        # Show all cards
        show_all(Player_hand,Dealer_hand)
        
        # Run different winning scenarios
        if Dealer_hand.value > 21:
            dealer_busts(Player_hand,Dealer_hand,Player_chips)
        elif Dealer_hand.value > Player_hand.value:
            dealer_wins(Player_hand,Dealer_hand,Player_chips)
        elif Dealer_hand.value < Player_hand.value:
            player_wins(Player_hand,Dealer_hand,Player_chips)
        else:
            push(Player_hand,Dealer_hand)
            
    # Inform Player of their chips total 
    print(f"Player winnings are {Player_chips.total}")
    
    # Ask to play again
    new_game = input("Do you want to play again ? yes: 'y' or no: 'n'") 
    if new_game[0].lower() == 'y':
            playing = True
            continue
    else:
        print("Thank you for playing this game !")
        break