# 직사각형 특징
# x, y가 똑같은게 2개 있음
# 비교해서 x, y가 하나인거를 2개로 만들면 됨

li_x = []
li_y = []

j = 0
p = 0

count_x = {}
count_y = {}

for i in range(3):
    a, b = map(int, input().split())
    li_x.append(a)
    li_y.append(b)

# for i in li_x:
#     try:
#         count_x[i] += 1
#     except:
#         count_x[i] = 1

# for i in li_y:
#     try:
#         count_y[i] += 1
#     except:
#         count_y[i] = 1

# print(count_x)
# print(count_y)

for i in li_x:
    one = li_x.count(i)
    if one == 1:
        j = i

for i in li_y:
    one = li_y.count(i)
    if one == 1:
        p = i

print("j:", j)
print("p:", p)

print(j, end=' ')
print(p, end='')