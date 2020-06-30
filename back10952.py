import sys

while(True):
    number = sys.stdin.readline().split()
    a = int(number[0])
    b = int(number[1])
    if (a == 0 and b == 0): 
        break
    else:
        print(a + b)