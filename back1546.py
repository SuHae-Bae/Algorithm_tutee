N = int(input())
grade = list(map(int, input().split()))
best = max(grade)
print("grade: ", grade)
print(best)
grade_calculated = []
for item in grade:
    grade_calculated.append((item/best)*100)


print("grade calculated: ", grade_calculated)
print("avg: ", sum(grade_calculated)/N)