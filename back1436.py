n = int(input())
# 이거 기억하자
# natural_number_set = set(range(1, 10001))

cnt = 0
m = 666
while(n > 0):
    if "666" in str(m):
        cnt += 1
    if cnt == n:
        print(m)
        break
    m += 1
    