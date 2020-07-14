N = int(input())
answer = N
li = []
cnt = 0
for i in range(N):
    word = input()
    for j in range(1, len(word)):
        print("j-1: ", word.find(word[j-1]))
        print("j: ", word.find(word[j]))
        if word.find(word[j-1]) > word.find(word[j]):
            answer -= 1
            break

print(answer)
