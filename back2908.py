n,m = input().split()
a = n[0]
b = n[1]
c = n[2]
x = m[0]
y = m[1]
z = m[2]
n1 = int(c+b+a)
print(n1)
m1 = int(z+y+x)
print(m1)
if n1 > m1:
    print(n1)
else:
    print(m1)