# 5*x + 3*y = N 을 만족하는
# x와 y의 최솟값

N = int(input())
# x = 0
# y = 0
li = []
for y in range ((N//3)+1):
    for x in range( (N//5)+1 ):
        if ((5*x + 3*y) == N):
            li.append(x + y)
        
if not li:
    print(-1)
else:
    print(min(li))

# x = N//5
# remain = N%5

# if remain != 0:
#     while x >= 0:
#         if x >= 0:
#             if remain%3 == 0:
#                 y = remain // 3
#                 break
#             x -= 1
#             remain += 5
# ans = x + y

# if ans < 1:
#     ans = -1
# print(ans)