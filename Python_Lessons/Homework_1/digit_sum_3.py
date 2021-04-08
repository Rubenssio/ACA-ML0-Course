num = int(input('Enter the number: '))

a = num % 10
b = num % 100 // 10
c = num // 100

print('The sum of the digits is:', a + b + c)

# # Another solution
# num = input('Enter the number: ')
#
# print('The sum of the digits is:', int(num[0]) + int(num[1]) + int(num[2]))
