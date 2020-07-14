s = input().lower()
alphabet = list(set(s))
cnt = []
# lower(), upper() 을 사용하면 소문자/대문자로 변환 가능

for i in alphabet:
    count = s.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2 :
    print("?")
else:
    print(alphabet[cnt.index(max(cnt))].upper())

