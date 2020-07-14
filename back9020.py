import sys

def check(num):
    if num == 1:
        return False
    else:
        # 2부터 num까지의 제곱근까지만 검사하면 됨
        # 안그러면 시간초과가 뜸
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

T = int(input())

for i in range(T):
    n = int(input())
    a = n//2
    b = a
    while a > 0:
        if check(a) and check(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1