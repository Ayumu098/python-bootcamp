# TODO: Ask the user how many items will be calculated
input_count = int(input("How many items will you enter? "))
total = 0

# TODO: Use a for loop to ask for more than one cost and count
for i in range(input_count):
    item_cost = int(input(f"Enter cost of item {i+1}: "))
    item_count = int(input(f"Enter quantity of item {i+1}: "))
    item_total = item_cost * item_count
    total += item_total

print(f"The total cost is: {total}")

