N = int(input())

for i in range(N):
    a, b, c = map(int, input().split())
    room_no = c//a + 1
    height = c%a
    if height == 0:
        print(a*100 + (room_no - 1))
    else:
        print(height*100 + room_no)


