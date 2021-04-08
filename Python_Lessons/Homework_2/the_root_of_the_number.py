num = int(input('Enter the number: '))

root = num

while root > 9:
    num = root
    root = 0
    while num != 0:
        root += num % 10
        num //= 10

print(root)
