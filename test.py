Purchase_history = []
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
}
]
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])
while best_buy_items:
    Purchase_history.append
    Purchase = input("What would you like to buy?")
    if Purchase == "Macbook":
        print("added to cart", Purchase)
    elif Purchase == "Hp laptop":
        print("added to cart", Purchase)
    else:
        print("added to cart", Purchase)
    Continue = input("Do you wish to continue?")
    if Continue == "no":
        break
    elif Continue == "yes":
        Purchase = input("What else would you like to buy?")
        break
print(Purchase)
