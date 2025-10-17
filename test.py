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
 
purchase = input("What would you like to buy?")
if purchase == "Macbook":
    print(best_buy_items[0]["name"])
    print(best_buy_items[0]["price"])
    print(best_buy_items[0]["department"])
    print(best_buy_items[0]["description"])
elif purchase == "Hp laptop":
    print(best_buy_items[1]["name"])
    print(best_buy_items[1]["price"])
    print(best_buy_items[1]["department"])
    print(best_buy_items[1]["description"])
else:
    purchase == "Lenovo Chromebook 14 laptop", 
    print(best_buy_items[2]["name"])
    print(best_buy_items[2]["price"])
    print(best_buy_items[2]["department"])
    print(best_buy_items[2]["description"])