a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

if a1 <= b1:
    min1 = a1
    max1 = b1
else:
    min1 = b1
    max1 = a1

if a2 <= b2:
    min2 = a2
    max2 = b2
else:
    min2 = b2
    max2 = a2

if max1 < max2 and max1 < min2 or min1 > min2 and min1 > max2:
    print(0)
elif max1 < max2:
    if min1 < min2:
        print(max1 - min2)
    else:
        print(max1 - min1)
elif min1 < min2:
    print(min2 - min1)
else:
    print(min1 - min2)
