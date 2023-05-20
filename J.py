while True:
    n = int(input())
    if n == 0:
        break
    i = 1
    res = []
    while i*i <= n:
        res.append(str(i*i))
        i += 1
    
    print(" ".join(res))