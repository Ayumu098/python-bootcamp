with open('sample.txt', 'r') as file:
    user_input = file.read().splitlines()
    print(user_input)