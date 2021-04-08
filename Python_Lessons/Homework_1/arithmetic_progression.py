a1 = int(input('FIRST member of the progression: '))
a2 = int(input('SECOND member of the progression: '))
n = int(input('Please enter the n: '))

step = a2 - a1
a_n = a1 + (n - 1) * step

print('The n-th member of this progression is:', a_n)
