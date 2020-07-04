li = []
for i in range(5):
    num = int(input())
    if num <= 40:
        li.append(40)
    else:
        li.append(num)

print(round(sum(li)/5))
