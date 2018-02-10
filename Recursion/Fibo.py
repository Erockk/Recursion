

def fib():
    a = 0;
    b = 1;
    c = 0;


    for x in range (0, 12):
        a = b;
        b = c;
        c = a + b;

        print(c);




fib()