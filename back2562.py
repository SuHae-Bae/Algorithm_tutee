li = []
for i in range(9):
    n = int(input())
    li.append(n)

b = max(li)
c = li.index(b) + 1

print(b)
print(c)