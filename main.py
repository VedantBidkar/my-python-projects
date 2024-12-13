import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${bid_amount}.")

database = {}
Continue_bidding = True
while Continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("enter the price: $"))
    database[name] = bid
    should_continue = input("Are there any other bidders?(yes/no): \n").lower()
    if should_continue == "no":
        Continue_bidding = False
        find_highest_bidder(database)
    elif should_continue == "yes":
        print("\n" * 20)





