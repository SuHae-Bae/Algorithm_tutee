n = int(input())
count = 2*n - 1
a = 1
for i in range(count): 
    if i <= n - 1:
        print("*"*a)
        a += 1
        # print("i: ", i)
        # print("a: ", a)
    else:
        a -= 1
        print("a: ", a)
        print("*"*(a-1))
        # print("i: ", i)
        # print("a: ", a)