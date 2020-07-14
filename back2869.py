A, B, V = map(int, input().split())

# nA - nB = V
# n(A-B) = V
# n = V/(A-B)


# a = 0
# cnt = 0
# while a < V:
#     a += A
#     a -= B
#     if a == V:
#         break
#     cnt += 1

# print(cnt)

up = A - B
cnt = (V - A) // up

if A >= V:
    print(1)

# 낮에 올라간 거리와 나무의 높이가 같거나 
# 낮에 올라간 거리보다 나무의 높이가 낮은 경우는 위에서 정의해줬으므로 
# 여기서는 그 경우를 제외하고 생각함

elif (V - A) % up == 0:
    print(cnt + 1)
else:
    print(cnt + 2)