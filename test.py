""" def occupied(n,y,t):
    both = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            both +=1
    return both 
print(occupied(5, "CC..C", ".CC..")) """

""" Ex.(example): """
""" student = {
    'name': 'Cadee',
    'age' : 15, 
    'grades' : (80,90,100)
}
print(student['grades']) """

""" def password(x):
    upper = 0
    lower = 0
    digits = 0
    if len(x) > 6 and len(x) < 13:
        for char in x:
            if char.isdigit():
                lower += 1
            if upper> 3 and lower >2 and digits> 1 """

""" def wizard(o, n, duels):
    owner = 0
    number_of_owner = 1
    for i in duels:
        #"BA"
        if duels[1] == owner:
            owner = duels[0]
            number_of_owner += 1
    for i in range(n):
        if duels[i][1] == owner """






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
    "name": "Lenovo Chromebook 14 Laptop",
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