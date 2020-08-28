# import sys
# N = int(input())
# li = []
# for i in range(N):
#     x, y = sys.stdin.readline().split()
#     x = int(x)
#     li.append((x, y))

# print(li)

# li = sorted(li, key = lambda x : x[0])

# for i in range(N):
#     print(li[i][0], li[i][1])


member_num = int(input())
member_list = []

for _ in range(member_num):
    member_age, member_name = map(str, input().split())
    member_age = int(member_age)
    member_list.append((member_age, member_name))

#나이 숫자 정렬 > 가입순 정렬
member_list.sort(key = lambda member: (member[0]))

for member in member_list:
    print(member[0], member[1])