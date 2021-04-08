import math


N = int(input('Enter the number: '))

largest_int_pow_of_3 = 3 ** int(math.log(N, 3))

print(largest_int_pow_of_3)
