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

item = {
    "name": "Macbook",
    "price": 1299.99,
    "department": "Laptop",
    "description": "13-inch, 528GB."
}
print(item["name"])