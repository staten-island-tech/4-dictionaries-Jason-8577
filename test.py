""" def occupied(n,y,t):
    both = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            both +=1
    return both 
print(occupied(5, "CC..C", ".CC..")) """

def maximum(H,O,N,I,n):
    for i in range