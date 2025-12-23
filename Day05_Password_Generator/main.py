import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_list = []

for index in range(0,nr_letters):
    chosen_list.append(random.choice(letters))

for index in range(0,nr_symbols):
    chosen_list.append(random.choice(numbers))

for index in range(0,nr_numbers):
    chosen_list.append(random.choice(symbols))

visited = []
total_characters = nr_letters + nr_symbols + nr_numbers
password = ""

while len(password) < total_characters:
    index = random.randint(0,total_characters - 1)
    if index not in visited:
        password += chosen_list[index]
    visited.append(index)

print(f"Your Password : {password}")