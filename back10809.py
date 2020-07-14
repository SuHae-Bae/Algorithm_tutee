s = input()
alphabet = ["a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
answer = []

for i in alphabet:
    loc = s.find(i)
    answer.append(loc)

for i in range(len(answer)):
    print(answer[i], end = ' ')