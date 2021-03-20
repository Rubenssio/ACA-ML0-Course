txt = input('Enter the text: ')

letter_counts = {}

for char in txt:
    if char in letter_counts:
        letter_counts[char] += 1
    else:
        letter_counts[char] = 1

odd_counts = 0
impossible = False
middle_letter = None

for letter, count in letter_counts.items():
    if count % 2 != 0:
        odd_counts += 1
        middle_letter = letter
        if odd_counts > 1:
            impossible = True
            break

if impossible:
    print('impossible')
else:
    sorted_letters = sorted(letter_counts)

    palindrome_list = []

    for letter in sorted_letters:
        palindrome_list.append(letter * (letter_counts[letter] // 2))

    for item in palindrome_list:
        print(item, end='')
    print(middle_letter, end='')
    for item in palindrome_list[::-1]:
        print(item, end='')
    print()
