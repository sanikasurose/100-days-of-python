from art import logo

print(logo)
print("Welcome to the secret auction program.")

auction_data = {}
start = True

while start:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_data[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if others == "no":
        start = False
    elif others != "yes":
        print("Not a valid option, rerun program.")
        start = False

def compare_dictionary(auction_data):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in auction_data.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

compare_dictionary(auction_data)
