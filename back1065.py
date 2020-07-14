# 한수의 특징
# 1자리는 모두 한수로 인정을 해줌
# 2자리는 모두 한수임. 왜냐면 공차가 하나뿐이니까.
# 우리는 3자리 수만 비교해서 찾으면 됨
N = int(input())
cnt = 0
li = []
for i in range(1, N+1):
    li.append(i)

for i in li:
    if i < 100:
        cnt += 1
    else:
        if i == 1000:
            cnt += 0
        else:
            n = str(i)
            a = int(n[0])
            b = int(n[1])
            c = int(n[2])
            if a-b == b-c:
                cnt += 1
            else:
                cnt += 0

print(cnt)
        

