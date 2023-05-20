from math import sqrt
while True:
    try:
        a,b,c = list(map(int, input().split()))
        h = sqrt(144 + a**2)
        if (12/b) < (h/c):
            print("N")
        else:
            print("S")
    except EOFError:
        break