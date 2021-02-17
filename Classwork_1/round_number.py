num = float(input('Enter the number: '))

ans = int(num // 1)

if num - ans >= 0.5:
    ans += 1

print('The rounded number is:', ans)
