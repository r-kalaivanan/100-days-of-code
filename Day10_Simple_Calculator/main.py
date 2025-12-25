def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    while True:

        operand_one = int(input("What's your first integer : "))

        while True:
            operator = input("Pick the operator [ + , - , * , / ] : ")
            operand_two = int(input("What's the next integer : "))

            match operator:
                case '+':
                    answer = add(operand_one,operand_two)
                case '-':
                    answer = sub(operand_one,operand_two)
                case '*':
                    answer = mul(operand_one,operand_two)
                case '/':
                    answer = div(operand_one,operand_two)
                case _:
                    print("Invalid Operator!")

            print(f"{operand_one} {operator} {operand_two} = {answer}")
            choice = input("Type 'y' to continue / 'n' to start a new calculation / 'exit' to end! : ")
            if choice == 'y':
                operand_one = answer
            elif choice == 'n':
                break;
            elif choice == "exit":
                return "Calculation Ended!"
            else:
                return "Invalid Input!"

print(calculator())