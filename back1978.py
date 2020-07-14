N = int(input())
li = list(map(int, input().split(' ')))
ans = 0


# 어떤 수 X가 소수 인지를 판별하려면 
# X를 2부터 X보다 작은 수(X-1)까지 
# 차례대로 나누어 떨어지는지 검사하면 됩니다
if len(li) == N: 
    for i in li:
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            ans += 1

print(ans)



