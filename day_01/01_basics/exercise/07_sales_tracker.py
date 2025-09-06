item_cost_1 = int(input("Item cost 1: "))  # Let the user enter a number
item_count_1 = int(input("Item count 1: "))  # Let the user enter a number

item_cost_2 = int(input("Item cost 2: "))  # Let the user enter a number
item_count_2 = int(input("Item count 2: "))  # Let the user enter a number

item_cost_3 = int(input("Item cost 3: "))  # Let the user enter a number    
item_count_3 = int(input("Item count 3: "))  # Let the user enter a number  

#calculate total sales
total_sales = (item_cost_1 * item_count_1) + (item_cost_2 * item_count_2) + (item_cost_3 * item_count_3)
print("Total sales: ", total_sales)
