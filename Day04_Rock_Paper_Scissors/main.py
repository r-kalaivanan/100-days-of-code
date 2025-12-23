rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#rock = 0
#paper = 1
#scissors = 2

import random

ascii_art = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissors Game!\n")

play = True
while play:

    player_choice = int(input("What do you choose [Rock : 0, Paper : 1, Scissors : 2] : "))
    computer_choice = random.randint(0, 2)

    print("You chose :\n", ascii_art[player_choice])
    print("Computer chose:\n", ascii_art[computer_choice])
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 0:
        if computer_choice == 1:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    elif player_choice == 1:
        if computer_choice == 2:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    elif player_choice == 2:
        if computer_choice == 0:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    else:
        print("Invalid Choice!")

    choice = input("Wanna go again [y/n] : ")
    if choice == "n":
        play = False

print("Thanks for playing!")


