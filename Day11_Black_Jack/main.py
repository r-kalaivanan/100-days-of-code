import random

black_jack = [11,1,2,3,4,5,6,7,8,9,10,10,10]

def card_deck(limit):
    deck = []
    for index in range(0,limit,1):
        deck.append(random.choice(black_jack))
    return deck

def result(player_sum,computer_sum):
    if player_sum > 21:
        print(f"Your score is greater than 21!... You Lose!")
    elif player_sum == computer_sum:
        print("It's a draw!")
    elif player_sum > computer_sum:
        print("You win!")
    else:
        print("Computer Wins!")
    return

def print_result(player_cards,computer_cards):
    print(f"Your Deck : {player_cards}")
    print(f"Final Score : {sum(player_cards)}\n")
    print(f"Computer Deck : {computer_cards}")
    print(f"Final Score : {sum(computer_cards)}\n")
    result(sum(player_cards), sum(computer_cards))
    return


def game():

    print("Welcome to Black Jack!\n")

    while True:

        player_cards = card_deck(2)
        computer_cards = card_deck(2)
        if sum(computer_cards) <= 16:
            computer_cards.append(random.choice(black_jack))

        print(f"Your Cards : {player_cards}")
        print(f"Computer Card : {computer_cards[0]}")

        choice = input("Do you wanna draw another card [y/n] : ")
        if choice == 'y':
            player_cards.append(random.choice(black_jack))
            print_result(player_cards,computer_cards)
        elif choice == 'n':
            print_result(player_cards[0:2], computer_cards)
        else:
            print("Invalid Choice!")

        if input("Do you wanna go again [y/n] : ") == 'n':
            break

    return

game()
print("Thanks for playing!")

