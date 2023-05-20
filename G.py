from math import sqrt
def getsum(n):
    s = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            s += i
            if 1 < i < sqrt(n):
                s += n//i
    return s
n = int(input())
while True:
    m = getsum(n)
    nc = getsum(m)
    if nc == n:
        print(n + m)
        break
    else:
        n -= 1