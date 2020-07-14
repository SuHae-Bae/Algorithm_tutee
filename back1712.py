A, B, C = map(int, input().split())

# i = 1

# while ((A + B*i) >= C*i):
#     i += 1
#     if ((A + B*i) < C*i):
#         print(i)
#         break

# print(i)


# A + Bi < Ci 를 만족하는 i를 구해야 함
# A < (C - B)i
# A / (C - B) < i 
# 이 식에서 분모가 음수가 되면 안되므로 C >= B여야 한다.
# 또한 0원은 수익이 아니므로 A/(C-B)에 1을 더해주면 된다.
if B < C:
    print((A//(C - B)) + 1)
else:
    print(-1)