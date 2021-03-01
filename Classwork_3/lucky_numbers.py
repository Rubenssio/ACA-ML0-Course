num = input()

sum1 = 0
sum2 = 0

for char in num[::2]:
    sum1 += int(char)

for char in num[1::2]:
    sum2 += int(char)

if sum1 == sum2:
    print('Yes')
else:
    print('No')
