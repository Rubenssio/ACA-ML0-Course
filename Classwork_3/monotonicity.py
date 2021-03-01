def monotonicity(list1, n):
    ascending = True
    descending = True

    for i in range(n - 1):
        if descending and list1[i] <= list1[i + 1]:
            descending = False
        if ascending and list1[i] >= list1[i + 1]:
            ascending = False

    if ascending:
        return 'Ascending'
    if descending:
        return 'Descending'
    return 'Neither'

N = int(input())

num_list = [int(n) for n in input().split()]

print(monotonicity(num_list, N))
