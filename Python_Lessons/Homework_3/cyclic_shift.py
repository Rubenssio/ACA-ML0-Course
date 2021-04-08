N, k = [int(n) for n in input().split()]

S = [int(n) for n in input().split()]

for _ in range(k//N):
    S = S[-1:].extend(S[:-1])

for num in S:
    print(num, end=' ')

print(1000%3)