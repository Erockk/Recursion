""" This is a recursion and non recursion practice project in python
    Created by Erik Olson"""

def fib():
    a = 0
    b = 1
    c = 0


    for x in range (0, 12):
        a = b
        b = c
        c = a + b

        print(c)

def fibRecursion(n):


    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecursion(n-2) + fibRecursion(n-1)


fib()
print("\nRecursion: ", fibRecursion(12))
