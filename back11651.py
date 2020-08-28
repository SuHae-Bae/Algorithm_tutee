import sys
N = int(sys.stdin.readline())
li = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))


# print(li)
# 좌표 정렬 하는법(sorted() 활용)
# 인자 없이 그냥 sorted()를 사용하면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.
# 좌표일 경우, x를 기준으로 오름차순으로 정렬하며, x가 같을 경우 y를 기준으로 오름차순으로 정렬한다.
# key인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
# key인자에서 x[0]은 x좌표를, x[1]은 y좌표를 의미한다.

# 예를 들어, sorted(a, key = lambda x : x[0]) 를 할 경우,
# a에 있는 좌표들이 x[0], 즉 x좌표를 기준으로 오름차순으로 정렬된다.
# 만약 sorted(a, key = lambda x : x[1])를 할 경우, 
# a에 있는 좌표들이 x[1], 즉 y좌표를 기준으로 오름차순으로 정렬된다.

# 아이템 첫 번째 인자(x)를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자(y)를 기준으로 내림차순으로 정렬하려한다면,
# sorted(a, key = lambda x : (x[0], -x[-1])) 
# 으로 정렬할 수 있다.

a = sorted(li, key = lambda x: (x[1], x[0]))

for i in a:
    print(i[0], i[1])