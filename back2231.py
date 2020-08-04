n = int(input())
ans = 0

for i in range(1, n+1):
    li = list(map(int, str(i)))
    ans = i + sum(li)

    if ans == n:
        print(i)
        break
    
    if i == n:
        print(0)
