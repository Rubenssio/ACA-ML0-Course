def string_power(s, k):
    if k >= 0:
        return s * k

    k = -k
    segment = s[:len(s)//k]

    if segment * k == s:
        return segment

    return "undefined"


string_s = input('Input string S: ')
the_k = int(input('Input the K: '))

print(string_power(string_s, the_k))
