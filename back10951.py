import sys

while(True):
    try:
        number = sys.stdin.readline().split()
        a = int(number[0])
        b = int(number[1])
        print(a + b)
    except:
        break