from art import logo

# FUNCTIONS
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def result(n1, n2, user_choice):
    result = operations[user_choice](n1, n2)
    print(f"Your answer is: {result}")
    return result

# VARIABLES AND DICTIONARIES
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# START OF PROGRAM

print(logo)

program_over = False
while not program_over:
    print("Welcome to the calculator.")
    start = input("Should we start? 'Y' or 'N'? ")
    if start == "Y":
        program_over = False
        n1 = int(input("Type in the first number: "))
        n2 = int(input("Type in the second number: "))
        user_choice = input(
            "Which operation do you want to do?\n1. +\n2. -\n3. *\n4. "
            "/\nEnter: ")
        result(n1, n2, user_choice)
    else:
        print("Okay, thank you.")
        program_over = True
