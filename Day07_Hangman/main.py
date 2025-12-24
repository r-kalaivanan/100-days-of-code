stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

word_list = ["aardvark", "baboon", "camel"]

game = True
while game:
    print("Welcome to Hangman!")

    word = random.choice(word_list)
    dash_string = ['_'] * len(word)
    list_word = list(word)
    print(list_word)
    wrong_count = len(stages)

    while True:
        print(f"Your Word : {''.join(dash_string)}")
        user_guess = input("Take a guess : ")
        indexes = [i for i, v in enumerate(list_word) if v == user_guess]
        if len(indexes) > 0:
            print("That's a right guess!")
            for index in range(0,len(indexes)):
                dash_string[indexes[index]] = user_guess
        else:
            print("That's a wrong guess!")
            if wrong_count >= 2:
                print(stages[wrong_count - 1])
            wrong_count -= 1

        if '_' not in dash_string:
            print(f"You've won. Your word {''.join(dash_string)}")
            break
        elif wrong_count == 0:
            print(stages[wrong_count])
            print(f"You are hanged man!")
            break

    choice = input("Wanna go one more time ? [y/n] : ")
    if choice == 'n':
        game = False

print("Thanks for playing, Man!")