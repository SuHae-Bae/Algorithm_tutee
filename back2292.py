# 1, 7, 19, 37, 
N = int(input())
start = 1
a = 6
cnt = 1

if N == 1:
    print(1)
else:
    while True:
        start += a
        cnt += 1
        if N <= start:
            print(cnt)
            break
        a += 6