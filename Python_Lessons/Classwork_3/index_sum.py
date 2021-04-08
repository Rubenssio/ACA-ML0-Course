N = int(input())
A = [float(n) for n in input().split()]
M = int(input())
IND = [int(n) for n in input().split()]

sum = 0

for i in IND:
    sum += A[i]

print(sum)
