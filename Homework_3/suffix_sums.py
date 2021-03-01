A = [float(n) for n in input().split()]

B = []

for i in range(len(A)):

    num_sum = sum(A[i:])

    if num_sum % 1 == 0:
        B.append(int(num_sum))
    else:
        B.append(num_sum)

for num in B:
    print(num, end=' ')
