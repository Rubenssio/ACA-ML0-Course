def is_palindrome(text):
    if text == text[::-1]:
        return True
    return False


a, b = [int(n) for n in input().split()]

pal_nums = []

if b < a:
    print('First number must be less than or equal to the second number')
else:
    for i in range(a, b + 1):
        if is_palindrome(str(i)):
            pal_nums.append(i)

    for num in pal_nums:
        print(num, end=' ')
