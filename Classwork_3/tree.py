n = int(input())

num_of_rows = int(n / 2 + 0.5)

for i in range(num_of_rows):
    spaces = num_of_rows - i
    print(' ' * spaces + '*' * (i * 2 + 1))
