def is_prime(num):

    if num == 2:
        return True

    if num % 2 == 0 or num == 1:
        return False

    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
            return False
    return True


def goldbach_s_conjecture(even_num):

    if even_num < 3:
        return f'The number {even_num} is not bigger than 2'

    if even_num % 2 != 0:
        return f'The number {even_num} is not even'

    if even_num == 4:
        return [(2, 2)]

    about_quarter = even_num // 4 + even_num // 2 % 2

    goldbach_primes = []

    for i in range(1, about_quarter):
        a = i * 2 + 1
        b = even_num - a
        if is_prime(a) and is_prime(b):
            goldbach_primes.append((a, b))

    return goldbach_primes


number = int(input())

if number > 10000:
    print('This program is limited to checking a number only up to 10000')

else:
    GC_primes = goldbach_s_conjecture(number)

    if type(GC_primes) != list:
        print(GC_primes)
    else:
        print('All possible pairs')
        for prime_pair in GC_primes:
            print(f'{prime_pair[0]} {prime_pair[1]}')
