a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print('Non-quadratic equation')
    if b != 0:
        print('One solution: ', -c / b)
    else:
        if c != 0:
            print('No solutions')
        else:
            print('Infinite solutions')
else:
    print('Quadratic equation')
    discriminant = b ** 2 - 4 * a * c
    print('Discriminant: ', int(discriminant))
    if discriminant < 0:
        print('No solutions')
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('Tow solutions:', x1, x2)
