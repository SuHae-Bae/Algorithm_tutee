# 오답 1
# import sys
# N = int(input())
# a = map(int, input().split())
# li = []

# for i in range(N):
#     li.append(a[i])

# b = min(li)
# c = max(li)

# print(b, c)

# 오답 2
# import sys

# N = int(input())
# a = sys.stdin.readline().split()
# li = []

# for i in range(N):
#     li.append(a[i])

# b = min(li)
# c = max(li)

# # b = min(a)
# # c = max(a)

# print(b, c)

N = int(input())
li = list(map(int, input().split()))
print(min(li), max(li))