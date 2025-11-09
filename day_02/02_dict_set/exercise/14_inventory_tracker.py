import json

def add(inventory):
    """TODO:
        / Ask for item name, info, and stock
        / Create a dictionary with key: name, info, stock
        / Add that dictionary to inventory
    """

    name = input("Enter item name: ")
    info = input("Enter item info: ")
    stock = int(input("Enter item stock: "))

    item = {
        "name": name,
        "info:": info,
        "stock": stock,
    }

    inventory.append(item)

def remove(inventory):
    """TODO:
        / Ask for item index (int)
        / Remove item in that index in inventory
    """
    index = int(input("Enter index: "))
    inventory.pop(index)

def read(inventory):
    """TODO:
        / Ask for item index (int)
        / Show item in that index in inventory
    """
    index = int(input("Enter index: "))
    print(inventory[index])

def print_item(item):
    for field, details in item.items():
        print(f"\t{field}: {details}")

def show(inventory):
    for item in inventory:
        print_item(item)

def save(inventory):
    # Open the file
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)

def load():
    with open('inventory.json', 'r') as file:
        return json.load(file)

def main():
    """Created to test functions"""
    running = True
    inventory = []

    while running:
        command = input("Command: ")

        if command == "add":
            add(inventory)
        elif command == "remove":
            remove(inventory)
        elif command == "read":
            read(inventory)
        elif command == "show":
            show(inventory)
        elif command == "save":
            save(inventory)
        elif command == "load":
            inventory = load()
        elif command == "exit":
            running = False

main()
