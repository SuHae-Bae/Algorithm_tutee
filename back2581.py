M = int(input())
N = int(input())
li = []

for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
        li.append(i)

if len(li) > 0:
    print(sum(li))
    print(li[0])
else:
    print(-1)
