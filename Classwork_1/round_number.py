num = float(input('Enter the number: '))

ans = num // 1 + (num % 1 + 0.5) // 1

print('The rounded number is:', int(ans))
