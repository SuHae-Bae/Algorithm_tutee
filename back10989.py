# N = int(input())
# li = []
# cnt = []
# for i in range(N):
#     li.append(int(input()))

# print("li: ", li)

# # 카운팅 정렬을 사용해서 해결해보라고 함
# # 카운팅 정렬은 해당 숫자가 몇번 등장하는지 누적해서
# # 많은순서대로 정렬

# # 먼저 특정 숫자가 몇개 들어있는지 알아보기 위해
# # unique한 값만 뽑아서 새로운 배열에 넣어줌
# li_1 = list(set(li))
# print("li_1: ", li_1 )

# # 그 다음 count를 해서
# # 해당 숫자의 수량을 cnt 배열에 넣어줌
# for i in li_1:
#     cnt.append(li.count(i))
# print("cnt: ", cnt)

# li_2 = []
# num = 0
# for i in cnt:
#     while i > 0:
#         li_2.append(li_1[num])
#         i -= 1    
#     num += 1

# print("li_2:", li_2)
    

import sys

# 10000번까지 모두 0을 갖는 배열을 생성한다
N = int(input())
cnt_list = [0] * 10001

# cnt_list에 입력받은 숫자의 위치에 입력받을 때 마다 +1을 해준다
for i in range(N):
    cnt_list[int(sys.stdin.readline())] += 1

# 정규표현식
# 10000번 동안
# %s: 문자열로
# \n: 줄을 바꿔서 출력(한줄씩 출력)
# i를 cnt_list[i]번만큼 출력한다
# 종합하자면 i를 cnt_list[i]번만큼 문자열로 줄을 바꿔서 출력(한줄씩 출력)
for i in range(10001):
    sys.stdout.write(('%s\n' % i * cnt_list[i]))