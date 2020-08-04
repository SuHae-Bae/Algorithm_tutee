N, M = map(int, input().split())
ans = []

li = list(map(int, input().split(' ')))

for i in range(N-2):
    for j in range(i+1, N-1):
        for p in range(j+1, N):
            if li[i] + li[j] + li[p] <= M:
                ans.append(li[i] + li[j] + li[p])

print(max(ans))
