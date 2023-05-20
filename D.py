from calendar import c


n, r = list(map(int, input().split()))
cluters = {}

for i in range(n):
    x, y = list(map(int, input().split()))

    if y in cluters:
        for j in range(len(cluters[y])):
            if abs(cluters[y][j]-x) > r:
                cluters[y].append(x)
                break
            else:
                cluters[y][j] = int((cluters[y][j]+x)/2)
                break
    else:
        cluters[y] = [x]
c = 0
for i in cluters:
    c += len(cluters[i])
print(c)

for i in cluters:
    for j in cluters[i]:
        print(j, i)