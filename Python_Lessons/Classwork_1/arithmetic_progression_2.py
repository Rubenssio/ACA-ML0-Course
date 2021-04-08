n = int(input('n = '))
a_n = int(input('a_n = '))
m = int(input('m = '))
a_m = int(input('a_m = '))
k = int(input('k = '))

d = (a_m - a_n) / (m - n)

a1 = a_n - (n - 1) * d

a_k = a1 + (k - 1) * d

print('Answer:')
print('a_k =', a_k)
