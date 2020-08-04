# Merge sort를 사용해서 정렬해보려고 함

N = int(input())
li = []

for i in range(N):
    li.append(int(input()))

def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(li1, li2):
    ans = []
    i=0;j=0
    while(i<len(li1) and j<len(li2)) :
        if li1[i]<=li2[j] :
            ans.append(li1[i])
            i+=1
        else :
            ans.append(li2[j])
            j+=1
    if i==len(li1) : 
        ans = ans + li2[j:len(li2)]
    if j == len(li1): 
        ans = ans + li1[i:len(li1)]
    return ans


m = merge_sort(li)
print(*m, sep="\n")