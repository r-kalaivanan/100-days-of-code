import random
import game_data

def get_random(visited):
    available = [d for d in game_data.data if d['name'] not in visited]
    return random.choice(available)

def game():
    print("Welcome to Higher or Lower!, Let's start!...\n")

    while True:
        visited = []
        choice_one = random.choice(game_data.data)
        visited.append(choice_one['name'])
        score = 0

        while len(visited) < len(game_data.data):

            choice_two = get_random(visited)
            visited.append(choice_two['name'])

            print(f"A : {choice_one['name']}, {choice_one['description']}, {choice_one['country']}")
            print(f"B : {choice_two['name']}, {choice_two['description']}, {choice_two['country']}")

            guess = input("\nGuess who has more follower count : ")
            if choice_one['follower_count'] > choice_two['follower_count']:
                higher = 'A'
            else:
                higher = 'B'

            if guess == higher:
                if higher == 'B':
                    choice_one = choice_two
                score += 1
                print(f"Yep, That's correct!... Current Score : {score}\n")
            else:
                print(f"You Lose!... Your Score : {score}")
                break

        if len(visited) == len(game_data.data):
            print(f"Oops!. Ran out List!... You win!... Your Score : {score}")

        if input("\nWanna go again [y/n] : ") == 'n':
            return "\nThanks for playing!"

print(game())


