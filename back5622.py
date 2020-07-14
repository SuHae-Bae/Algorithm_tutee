n = input()
# 알파벳 리스트 만드는 법
# from string import ascii_lowercase를 한 다음
# 소문자 리스트: list(ascii_lowercase)
# 대문자 리스트: list(ascii_uppercase)
li = []
li_1 = []
for i in n:
    if i == "A" or i == "B" or i == "C":
        li.append(2)
    elif i == "D" or i == "E" or i == "F":
        li.append(3)
    elif i == "G" or i == "H" or i == "I":
        li.append(4)
    elif i == "J" or i == "K" or i == "L":
        li.append(5)
    elif i == "M" or i == "N" or i == "O":
        li.append(6)
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        li.append(7)
    elif i == "T" or i == "U" or i == "V":
        li.append(8)
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
        li.append(9)

for i in li:
    li_1.append(i + 1)

print(sum(li_1))