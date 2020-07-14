# N = int(input())

# li = []



# for i in range(N):
#     k = int(input())
#     n = int(input())
#     v = [j for j in range(1, n+1)]
#     # 인덱스 무시
#     for _ in range(k):
#         print("v: ", v)
#         for p in range(k):
#             v[p] += v[p-1]
#             print(str(p)+"번째"+"v[p]:", v[p])
#             print(str(p-1)+"번째"+"v[p-1]:", v[p-1])
#     print(v[n-1])
        
# def sum_people(k, n):
#     total = 0
#     if k == 1:
#         for i in range(1, n+1):
#             total += i                              # 1층에서는 n호는 1부터 n까지의 합
#         return total
#     else:
#         for j in range(1, n+1):
#             total += sum_people(k-1, j)             # k층 n호는 k-1층 1호부터 n호까지의 합
#         return total
 
 
# for i in range(int(input())):
#     k = int(input())
#     n = int(input())
#     print(sum_people(k, n))


a = int(input())

for i in range(a):
    d = []
    k = int(input())
    n = int(input())
    d = [j for j in range(1, n+1)]

    for l in range(k):
        print("d:", d)
        for j2 in range(1, n):
            d[j2] += d[j2-1]
            print(str(j2)+"번째"+"d[j2]:", d[j2])
            print(str(j2 - 1)+"번째"+"v[j2 - 1]:", d[j2 - 1])
    print(d[n-1])


