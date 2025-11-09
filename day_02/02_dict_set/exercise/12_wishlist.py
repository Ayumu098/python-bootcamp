order = {
    "Name": "Laptop Stand",
    "Info": "Metallic stand",
    "Price": 1500,
    "Discounted": False
}

# dict -> print details
print("Order:")
for field, details in order.items():
    print(f"\t{field}: {details}")