N = input()
# 숫자를 하나하나 분리해서 리스트에 넣음(string 형태)
li = list(N)
# 분리했던 숫자들을 다시 int형으로 변환
li = list(map(int, li))
# 혹은 li = [int(i) for i in li]
# 내림차순으로 정렬
li.sort(reverse=True)
# 한 줄로 출력
li = list(map(str, li))
a = ""
for i in li:
    a += i
print(a)
