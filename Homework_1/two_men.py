first = int(input('The number of cans the first man has shot: '))
second = int(input('The number of cans the second man has shot: '))

# the logic
cans = first + second - 1
print(cans - first)
print(cans - second)

# # a simpler solution
# print(second - 1)
# print(first - 1)