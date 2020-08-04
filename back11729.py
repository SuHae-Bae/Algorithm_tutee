n = int(input())
def hanoi(n, a, b, c):
    # 원판이 하나일때는 그냥 1번에서 3번으로 옮기면 됨
    if n == 1:
        print ("n = 1, a, c: ", a, c)
    else:
        # 원판 n - 1개를 보조 기둥으로 이동
        # 여기서는 이동하고자 하는 기둥이 c, 
        # 보조 기둥이 b
        print('n-1, a, c, b: ', n-1, a, c, b)
        hanoi(n-1, a, c, b)
        # 가장 큰 원반을 목적지로 이동
        # print(a, c)
        print("n, a, c: ", n, a, c)
        # 보조 기둥(b)에 있는 원판들을 목적지로 이동
        print('n-1, b, a, c: ', n-1, b, a, c)
        hanoi(n-1, b, a, c)
# 최소 이동 횟수는 
# 원판이 하나가 더 적을 때의 이동횟수에 2를 곱하고 1을 더한 것과 같음
# 가장 아래의 원판만 제외하고 위의 원판들을 모두 다른 기둥으로 옮겼을 때의 이동횟수: P(n-1)
# 가장 큰 원판을 다른 원판으로 옮길 때의 이동횟수: 1
# 나머지 원판을 큰 원판 위로 옮길 때의 이동횟수: P(n - 1)
# 즉,  P(n) = 2 P(n-1) + 1
sum_hanoi = 1
for i in range(n - 1):
    sum_hanoi = sum_hanoi * 2 + 1
print(sum_hanoi)
hanoi(n, 1, 2, 3)

