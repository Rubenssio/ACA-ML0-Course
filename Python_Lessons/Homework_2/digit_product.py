n = input('Enter the number: ')

product = 1

for char in n:
    digit = int(char)
    if digit != 0:
        product *= digit

print(product)
