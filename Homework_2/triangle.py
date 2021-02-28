sides = [int(n) for n in input().split()]

a = min(sides)              # shortest side
c = max(sides)              # longest side
b = sum(sides) - a - c      # medium side

if a + b <= c:
    print('No Triangle')
else:
    a_squared_plus_b_squared = a ** 2 + b ** 2
    c_squared = c ** 2

    if a_squared_plus_b_squared == c_squared:
        print('Right Triangle')

    elif a_squared_plus_b_squared > c_squared:
        print('Acute Triangle')

    else:
        print('Obtuse Triangle')
