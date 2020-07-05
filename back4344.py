N = int(input())
for i in range(N):
    li_1 = []
    li_2 = []
    cnt = 0
    li_1 = list(map(int, input().split()))
    print("li_1: ", li_1)
    n = li_1[0]
    print("n: ", n)
    add_num = (sum(li_1) - n)/ n
    print("add_num: ", add_num)
    len_1 = len(li_1)
    li_2 = li_1[1:len_1]
    print("li_2: ", li_2)
    for j in li_2:
        if j > add_num:
            cnt += 1
        else:
            cnt += 0
    ans = round(((cnt/n)*100), 3)
    print("percent: ", "%0.3f" % ans + "%")
    
    
