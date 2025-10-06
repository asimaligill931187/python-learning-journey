import os




biding_cont=False

while not biding_cont:

    name_bidder=input("Enter name of beter:")
    Price=int(input("Please Enter the price:"))
    choice=input("Any other beder:: Yes or No::")
        
    bet_dictionary={}
    bet_dictionary[name_bidder]=Price
    
    
    highest_bid=0
    for high in bet_dictionary:
        bid_amount=bet_dictionary[high]
        
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=high
            
    
    
    if choice=="no":
        biding_cont=True
        print(f"The winner is {high} with a bid of {bid_amount}")
    else:
        os.system("cls")
    
        
    


