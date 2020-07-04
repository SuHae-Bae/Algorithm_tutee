li = []
for i in range(5):
    num = int(input())
    li.append(num)

a = li[0:3]
b = li[-2:]

print((min(a) + min(b))-50)