number = int(input())

boring = True
check = number % 10
number // 10


while number != 0:
    if check != number % 10:
        boring = False
        break
    check = number % 10
    number = number // 10

if boring:
    print('Boring')
else:
    print('Interesting')
