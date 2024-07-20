def take_bet(chips):
  while True:
   try: 
       chips.bet = int(input("Enter the bet chip amount: "))
   except ValueError:
       print("Please enter an integer number")
   else :
       if chips.bet > chips.total:
          print("Sorry ! you don't havr enough funds ") 
       else:
          break
   pass