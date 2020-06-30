# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오
# 명령은 총 5가지이다.
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수르 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다. 
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. 
# 첫째 줄에 주어지는 명령의 수 N개가 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 길이를 비교해서 list가 비었는지 안 비었는지를 확인하면 시간초과가 남
# 그래서 길이를 비교하는게 아니라 그냥 not a 로 판단하도록 함
# 명령어와 숫자(push의 경우)를 따로따로 입력할경우 시간초과가 남
# 그래서 push 3 같이 이렇게 한번에 명령어와 숫자를 입력하도록 함
# 위의 방법들을 사용해도 계속 시간 초과가 남 
# 문제를 해결하려면 input가 아니라 sys를 import해서 readline을 해야함
# eval 말고 그냥 int(input()) 해도 괜찮음
# 굳이 함수를 따로 만들 필요도 없음 걍 readline하면 다 해결됨

# 해결방안 1
# import sys

# def push(x):
#     a.append(x)

# def pop():
#     if not a:
#         print(-1)
#     else:
#         print(int(a.pop()))

# def size():
#     print(len(a))

# def empty():
#     if not a:
#         print(1)
#     else:
#         print(0)

# def top():
#     if not a:
#         print(-1)
#     else:
#         print(a[len(a)-1])

# N = eval(input())
# a = []

# for i in range(N):
#     order = sys.stdin.readline().split()
#     Option = order[0]
    
#     if Option == "push":
#         push(order[1])
#     elif Option == "pop":
#         pop()
#     elif Option == "size":
#         size()
#     elif Option == "empty":
#         empty()
#     elif Option == "top":
#         rop()

# 해결방안 2의 일부

# def push(x):
#     a.append(x)

# def pop():
#     if not a:
#         print(-1)
#     else:
#         print(int(a.pop()))

# def size():
#     print(len(a))

# def empty():
#     if not a:
#         print(1)
#     else:
#         print(0)

# def top():
#     if not a:
#         print(-1)
#     else:
#         print(a[len(a)-1])


# 해결방안 3

import sys

N = int(input())
a = []

for i in range(N):
    order = sys.stdin.readline().split()
    Option = order[0]
    
    if Option == "push":
        a.append(order[1])

    elif Option == "pop":
        if not a:
            print(-1)
        else:
            print(int(a.pop()))

    elif Option == "size":
        print(len(a))

    elif Option == "empty":
        if not a:
            print(1)
        else:
            print(0)

    elif Option == "top":
        if not a:
            print(-1)
        else:
            print(a[len(a)-1])