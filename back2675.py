T = int(input())

for i in range(T):
    li = []
    S = input().split()
    n = int(S[0])
    word = S[1]
    length = len(word)
    for i in range(length):
        a = word[i]*n
        li.append(a)
    len_2 = len(li)
    text = ""
    for i in range(len_2):
        text += li[i]
    print(text)

