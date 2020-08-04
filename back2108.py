import sys
# sys.stdin.readline()으로 입력받지 않으면 시간초과뜸
N = int(input())
li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))
# 산술평균: N개의 수들의 합을 N으로 나눈 값
# 소숫점 첫째자리에서 반올림하는법: round(n) 
# 이렇게 2번째 매개변수를 기입하지 않으면 된다
a = sum(li)/N
a = round(a)
print(a)
# 중앙값: N개의 수들을 증가하는 숫서로 나열했을때 중앙값 
li.sort()
num = N//2
mid = li[num]
print(mid)
# 최빈값: N 개의 수들 중 가장 많이 나타나는 값
# 몰랐는데 counter라는 함수를 import해서 사용하는 듯하다
from collections import Counter
# Counter는 리스트를 입력받아 dictionary형태로
# 요소와 갯수를 출력해준다
count_num = Counter(li)
# print(count_num)
most = count_num.most_common()
print("most:", most)

if len(li) > 1:
    if most[0][1] == most[1][1]:
        mod = most[1][0]

    else:
        mod = most[0][0]
else:
    mod = most[0][0]
print(mod)
# 범위: N개의 수들 중 최댓값과 최솟값의 차이
print(max(li) - min(li))


