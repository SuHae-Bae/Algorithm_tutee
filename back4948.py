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

natural_list = list(range(2, 246912))
decimal_list = []
for i in natural_list:
    if check(i):
        decimal_list.append(i)

num = int(sys.stdin.readline())

while num != 0:  
    count = 0
    for i in decimal_list:
        if num < i <= num*2:
            count += 1
    print(count)
    num = int(sys.stdin.readline())