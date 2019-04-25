# This function is from Part.2.D.1

def fib_between(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            print(a, end = '')
        a, b = b, a + b