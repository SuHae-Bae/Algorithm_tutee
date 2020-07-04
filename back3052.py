# set type 으로 변형해서 list에서 고유한 값만 가져올 수 있음
li_1 = []
li_2 = []
for i in range(10):
    li_1.append(int(input()))

for item in li_1:
    num = item%42
    li_2.append(num)

print("li_1: ", li_1)
print("li_2: ",li_2)

# set 형은 indexing이 안되는 등의 제약이 있기 때문에 
# list형태로 다시 되돌려주면 좋음

li_3 = list(set(li_2))
print("li_3: ", li_3)
print("len(li_3)): ", len(li_3))