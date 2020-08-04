# 해결 전략
# 먼저 각자의 rank는 최초에 1임
# 비교하면서 자기보다 큰게 있을 경우 +1을 함

import sys

N = int(input())
info = []

for i in range(N):
    a, b = map(int, input().split())
    info.append((a, b))

for i in info:
    rank = 1

    for j in info:
        if (i[0] != j[0]) & (i[1] != j[1]):
            if (i[0] < j[0]) & (i[1] < j[1]):
                rank += 1

    print(rank)