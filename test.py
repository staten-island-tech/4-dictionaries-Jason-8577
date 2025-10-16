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

item = {
    "name": "Macbook",
    "price": 1299.99,
    "department": "Laptop",
    "description": "13-inch, 528GB."
}
{
    "name": "Hp laptop",
    "price": 799.99,
    "department": "Laptop",
    "description": "15-inch, 256GB."
}
print(item["name"][2])