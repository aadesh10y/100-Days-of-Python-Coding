import logo
print(logo.art)

# name = input("What is your name: ")
# bid = float(input("What is your bid?\n $"))

# bids = {}
# bids[name]= bid

# new_bid = input("Are there any other bidders? Types 'yes' or 'no':\n ")

# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name: ")
#     bid = float(input("What is your bid?\n $"))
#     bids[name] = bid
#     new_bid = input("Are there any other bidders? Types 'yes' or 'no':\n ").lower()
#     if new_bid == "no":
#         continue_bidding = False
#         highest_bidder(bids)

def highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bidding of ${highest_bid} ")   
    
 
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    bid = float(input("What is your bid?\n $"))
    bids[name] = bid
    new_bid = input("Are there any other bidders? Types 'yes' or 'no':\n ").lower()
    if new_bid == "no":
        continue_bidding = False
        highest_bidder(bids)  
    elif new_bid == "yes":
        print("\n" * 50)      