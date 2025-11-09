import json

data = [
    {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'},
]

with open('people.json', 'r') as file:
    read_data = json.load(file)
    print(type(data))