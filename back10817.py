import sys

# 틀림
# number = input().split()
# a = min(number)
# b = max(number)
# number.remove(a)
# number.remove(b)
# print(number[0])

# sort함수를 사용하는 방법도 있음
a = map(int, input().split())
b = sorted(a)
print(b[1])

# 가장 기본적으로 푸는 방법
a, b, c = map(int, input().split(' '))
if a >= b:
    if a >= c:
        if b >= c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b >= c:
        if c >= a:
            print(c)
        else:
            print(a)
    else:
        print(b)

# max와 min을 사용하여 풀기
a, b, c = map(int, input().split(' '))
max_abc = max(a, b, c)
min_abc = min(a, b, c)
print(a + b + c - max_abc - min_abc)