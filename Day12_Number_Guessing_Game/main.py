import random

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 3

def check_guess(guess,answer,turns):
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it!. The answer is {answer}.")
        return -1


def set_difficulty(mode):
    if mode == "easy":
        return EASY_LEVEL_TURNS
    elif mode == "hard":
        return HARD_LEVEL_TURNS
    else:
        return "Invalid Input!"

def game():

    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100!")
    mode  = input("Select a difficulty mode [easy/hard] : ")
    answer = random.randint(1,100)

    turns = set_difficulty(mode)

    while True:
        guess = int(input("Make a guess : "))
        turns = check_guess(guess,answer,turns)
        if turns == -1:
            break
        elif turns == 0:
            print(f"You lose!. The answer is {answer}")
            break
        else:
            print(f"You have {turns} guesses left!")

game()
print("Thanks for playing!")
