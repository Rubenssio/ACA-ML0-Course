def find_num_of_divs(n):

    num_of_divs = 0
    for i in range(1, n + 1):
        if n % i == 0:
            num_of_divs += 1

    return num_of_divs


def most_divs(a, b):

    has_the_most = a
    number_of_divs = 1

    for num in range(a, b + 1):

        new_num_of_divs = find_num_of_divs(num)

        if new_num_of_divs > number_of_divs:
            number_of_divs = new_num_of_divs
            has_the_most = num

    return has_the_most


a = int(input())
b = int(input())

has_the_most_divs = most_divs(a, b)

print(has_the_most_divs)
