n = list(map(int, input().split()))
n.sort()
a,b,c,d = n

if b-a < c < a+b or b-a < d < a+b or c-a < d < a+c or c-b < d < b+c:
    print("S")
else:
    print("N")