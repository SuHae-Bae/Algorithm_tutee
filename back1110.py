# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# 백준에 제출할 때는 print를 마지막 꺼 말고 다 지울것
N = int(input())
FirstNum = N
print("FirstNum: ", FirstNum)
count = 0
NewNum = 0

while(True):
    a = N//10
    b = N%10
    print("a: ", a)
    print("b: ", b)
    NewNum = a + b
    print("NewNum: ", NewNum)
    c = NewNum%10
    print("c: ", c)
    d = str(b) + str(c)
    d = int(d)
    count += 1
    print("d: ", d)
    N = d # 둘이 자리바꾸면 코드 안돌아감
    print("FirstNum: ", FirstNum)
    if (d == FirstNum):
        break
    
print(count)