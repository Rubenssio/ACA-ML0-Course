year = int(input('Please enter the year: '))

# տարբերակ 1
century = (year + 99) // 100

# # տարբերակ 2
# century = round(year / 100 + 0.49)

# # տարբերակ 3
# import math
# century = math.ceil(year / 100)

print(f'It is century: {century}')
