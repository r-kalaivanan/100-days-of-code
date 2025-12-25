import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to Blind Auction!")

while True:

    bids = {}
    max_bid = 0

    while True:

        name = input("Enter the bidder's name : ")
        amount = int(input("Enter the bid amount : "))

        bids[name] = amount

        if amount > max_bid:
            max_bid = amount

        if input("Is there an another bidder ? [\"yes\"/\"no\"] : ") == "no":
            break
        clear()

    clear()
    for key, value in bids.items():
        if value == max_bid:
            print(f"The winner is {key} with the maximum bid of {value}")
            break

    if input("\nWanna go another round ? [y/n] : ") == 'n':
        break
    clear()

print("\nThanks for playing!")