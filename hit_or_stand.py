def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("Tell if you want to stand or hit ? either 's' or 'h'")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("The player do not want to take an card")
            playing = False
        else :
            print("Pleae try again ")
            continue
        break