# 규칙1: 제곱수마다 새로운 숫자가 나타난다.
#        제곱수에서의 횟수는 제곱근*2 - 1
# 규칙2: 제곱수 + 1 부터 제곱수 + 루트 제곱수 까지 횟수가
#        루트 제곱수 * 2 로 같고,
#        그 뒤부터 다음 제곱수 - 1 까지 
#        루트 제곱수 * 2 + 1 로 같다.

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    length = y - x
    num = 1
    # 두 수의 차이보다 작은 제곱수 중 가장 큰 값을 찾아
    # num에 저장
    while True:
        if num**2 <= length < (num + 1) ** 2:
            break
        num += 1
    # 제곱수에서의 횟수는 제곱근*2 - 1
    if num**2 == length:
        print((num*2) - 1)
#   제곱수 + 1 부터 제곱수 + 제곱근 까지 횟수가
#   제곱근 * 2 로 같고,
    elif num ** 2 < length <= num ** 2 + num:
        print(num*2)
#   그 뒤부터 다음 제곱수 - 1 까지 
#   제곱근 * 2 + 1 로 같다.
    else:
        print((num*2) + 1)

