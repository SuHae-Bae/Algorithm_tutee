natural_number_set = set(range(1, 21))
generated_number_set= set()

print("natural_number_set: ", natural_number_set)
for i in range(1, 21):
    print("real i: ", i)
    for j in str(i):
        print("str(i): ", str(i))
        print("j: ", j)
        i += int(j)
        print("i: ", i)
    print("calculated i: ", i)
    generated_number_set.add(i)

print("generated_number_set: ", generated_number_set)
self_number_set = natural_number_set - generated_number_set

for i in sorted(self_number_set):
    print(i)