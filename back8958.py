# N = int(input())
# answer = []
# for i in range(N):
#     li = []
#     score = []
#     li = list(input())
#     # print(li)
#     n = len(li)
#     count = 0
#     for p in range(0, n - 1):
#         if li[p] == "O":
#             if li[p] == li[p+1]:
#                 if (p == n-2):
#                     # print("last: ", count)
#                     score.append(count + 1)
#                     score.append(count + 2)
#                 else:
#                     # print("p: ", p)
#                     # print("앞뒤같음: ", count)
#                     count += 1
#                     score.append(count)
#             else:
#                 # print("x나옴: ", count)
#                 score.append(count + 1)
#                 count = 0
#         else:
#             score.append(0)
#     answer.append(sum(score))
#     # print("score: ", score)
#     print(sum(score))

# # for i in answer:
# #     print(i)

n = int(input())
for i in range(n):
    li = input()
    score = 0
    count = 0
    for j in range(len(li)):
        if li[j] == 'O':
            count += 1
            score += count
            print("count: ", count)
            print("score: ", score)
        elif li[j] == 'X':
            score += 0
            count = 0
            print("count: ", count)
            print("score: ", score)
    print(score)