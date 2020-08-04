# bubble sort로 풀어보기
# 배열의 끝에서부터 2개씩 비교해서
# 앞에게 뒤에거보다 크면 위치를 바꿔줌

N = int(input())
li = []

for i in range(N):
    li.append(int(input()))

def swap(li, num1, num2):
    t = li[num1]
    li[num1] = li[num2]
    li[num2] = t

def bubble(li):
    num = len(li) - 1
    for i in range(num, 0, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                swap(li, j, j+1)

print("list: ", li)
bubble(li)
for i in li:
    print(i)