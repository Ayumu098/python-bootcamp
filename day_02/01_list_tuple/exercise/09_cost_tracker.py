def spend(expenses):
    expense = int(input("Enter expense: "))
    expenses.append(expense)


def refund(expenses):
    """TODO: Remove the last cost added (if any)"""

    empty = len(expenses) == 0
    if not empty:
        expenses.pop(-1)
    else:
        print("Warning: Expenses is empty")


def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)
    print("Total:", sum(expenses))


def save(expenses):
    file = open('receipt.txt', 'w')

    for expense in expenses:
        file.write(str(expense) + "\n")

    file.close()

def load():

    expenses = []

    with open('receipt.txt', 'r') as file:
        user_input = file.read().splitlines()

        for number in user_input:
            expenses.append(int(number))

        return expenses

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ").lower()
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "save":
            save(current_expenses)
        elif command=="load":
            current_expenses = load()

main()
