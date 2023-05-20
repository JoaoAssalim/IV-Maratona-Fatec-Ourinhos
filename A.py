n,l,c = list(map(int, input().split()))
s = input().split()

car = 0
line = 0
pag = 0

for i in s:
    if car + len(i) <= c:
        car += len(i)
    else:
        car = len(i)
        line += 1
    car += 1
    
    if line >= l:
        pag += 1
        line = 0
        

if car > 0:
    line += 1

if line > 0:
    pag += 1
    
print(pag)
        