print("Welcome to the tip calculator!")
bill = float(input("What is your total bill? $"))
tip_percentage = float(input("How much percentage for tip ? "))
split_number = int(input("How many numbers would you like to split? "))
total_bill = bill + bill * (tip_percentage / 100)
print("Each person should pay : $" + str(total_bill/split_number))
print(f"Each person should pay : ${total_bill/split_number}")

