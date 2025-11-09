# TODO: Fill in the details of the items you plan to buy
wishlist = [
    {
        "Name": "Laptop Stand",
        "Info": "Metallic stand",
        "Price": 1500,
        "Discounted": False
    },
    {
        "Name": "Mic",
        "Info": "Wireless",
        "Price": 4000,
        "Discounted": True
    },
    {
        "Name": "Coffee",
        "Info": "Baguio",
        "Price": 500,
        "Discounted": False
    }
]


def print_order(order):
    print("Order:")
    for field, details in order.items():
        print(f"\t{field}: {details}")

for order in wishlist:
    print_order(order)