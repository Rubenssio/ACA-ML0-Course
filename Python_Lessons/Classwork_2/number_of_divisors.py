x = int(input())

y = 2
number_of_divisors = 1

while y <= x:
    if x % y == 0:
        number_of_divisors += 1
    y += 1

print(number_of_divisors)
