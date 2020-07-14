# w - x,  h - y, x, y 
# 중 절댓값이 작은 값만큼 가면 될거같은데 
x, y, w, h = map(int, input().split())
li = []
num1 = abs(w - x)
num2 = abs(h - y)
num3 = x
num4 = y

li.append(num1)
li.append(num2)
li.append(num3)
li.append(num4)

print(min(li))