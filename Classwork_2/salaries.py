salary_1 = int(input())
salary_2 = int(input())
salary_3 = int(input())

min = 0
max = 0

if salary_1 < salary_2:
    min = salary_1
    max = salary_2
    if salary_3 < salary_1:
        min = salary_3
    elif salary_3 > salary_2:
        max = salary_3
else:
    min = salary_2
    max = salary_1
    if salary_3 < salary_2:
        min = salary_3
    elif salary_3 > salary_1:
        max = salary_3

print(max - min)
