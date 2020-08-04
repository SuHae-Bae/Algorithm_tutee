# 1. B로 시작할 때
# 홀수번째 줄의 짝수번째 칸이 B 여야 함(index가 0부터 시작)
# 짝수번째 줄의 홀수번째 칸이 B 여야 함
# 
# 2. W로 시작할 때
# 홀수번째 줄의 짝수번째 칸이 W 여야 함
# 짝수번째 줄의 홀수번째 칸이 B 여야 함 

def chess(box):
    n1 = 0

    # 검은색으로 시작할 때
    for i in range(8):
        for j in range(8):
            a = (0 if i in [0, 2, 4, 6] else 1)
            b = (0 if j in [0, 2, 4, 6] else 1)
            if (a == 0 and b == 0) or (a == 1 and b == 1):
                if ex[i][j] != "B" : 
                    n1 += 1
            if (a == 0 and b = 1) or (i == 1 and j == 0):
                if ex[i][j] != "W":
                    n1 += 1
        
        # 하얀색으로 시작할 때
        n2 = 0
        for i in range(8):
            for j in range(8): 
                a = (0 if i in [0, 2, 4, 6] else 1)
                b = (0 if j in [0, 2, 4, 6] else 1)
                if (a == 0 and b == 0) or (a == 1 and b == 1):
                    if ex[i][j] != "W" : 
                        n2 += 1
                if (a == 0 and b = 1) or (i == 1 and j == 0):
                    if ex[i][j] != "B":
                        n1 += 1
    
    return min(n1, n2)                    
        
n, m = map(int, input().split())
s = [list(input()) for i in range(n)]
print(s)
check = list()
for i in range(n - 7):
    for j in range(m - 7):
        box = [z[(0+j):(8+j)] for z in s[(0+i):(8+i)]]
        check.append(chess(box))

print(min(check))

