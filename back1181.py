import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
    li.append(input())

# 먼저 unique한 값만을 뽑아냄(중복제거)
a = list(set(li))

# 그 다음 sort를 통해 알파벳순으로 정렬함
a.sort()
print(a)
# 마지막으로 sort의 key를 len으로 주면 길이순으로 정렬됨
a.sort(key=len)

print(a)
for i in a:
    print(i)