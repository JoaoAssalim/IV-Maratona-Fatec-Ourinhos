p = ['L', "N", "O", "S"]
pos = 1
n = int(input())
s = input()
for i in s:
    if i == "D":
        pos -= 1
    else:
        pos += 1
    
    if pos >= 4:
        pos -= 4
    if pos < 0:
        pos += 4

print(p[pos])