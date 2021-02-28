number = int(input())

is_possible = False
check = number % 10
number = number // 10

while number != 0:
    if check > number % 10:
        is_possible = True
        break
    number = number // 10

if is_possible:
    print('Yes')
else:
    print('No')
    