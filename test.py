total = 0
cart = []
best_buy_items = [
{
    "name": "Macbook",
    "price": 1299.99,
    "department": "Laptop",
    "description": "13-inch, 528GB."
},
{
    "name": "Hp laptop",
    "price": 799.99,
    "department": "Laptop",
    "description": "15-inch, 256GB, touch screen."
},
{
    "name": "Lenovo Chromebook 14 laptop",
    "price": 249.99,
    "department": "Laptop",
    "description": "8 core, 4GB RAM, 128GB, touch screen, anti-glare."
},
]
Ask = input("Would you like to view the items?:")
if "yes" or "Yes" or "ye" or "Ye": 
    for key in best_buy_items:
        print(key)
else:
    print("Come again next time")
while True:
    Purchase = input("What would you like to buy?")
    cart.append(Purchase)
    if Purchase == best_buy_items["name"]:
        print(cart)