def make_palindrome1(txt):
    """using dictionary"""

    letter_counts = {}

    # let's make a dictionary with all the letters in the text (with counts)
    for char in txt:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    odd_counts = 0
    impossible = False
    middle_letter = None

    # let's see if there is more than one letter repeated odd times
    for letter, count in letter_counts.items():
        if count % 2 != 0:
            odd_counts += 1
            middle_letter = letter  # remembering the letter with odd count
            if odd_counts > 1:
                impossible = True
                break

    if impossible:
        return 'impossible'
    else:
        sorted_letters = sorted(letter_counts)

        palindrome_list = []

        # creating the first half of the palindrome as a list
        for letter in sorted_letters:
            palindrome_list.append(letter * (letter_counts[letter] // 2))

        # converting the list into a string
        palindrome_base = ''.join(palindrome_list)

        return ''.join((
            palindrome_base,
            middle_letter,
            palindrome_base[::-1]
        ))


def make_palindrome2(txt):
    """using set"""

    letters = set(txt)

    palindrome = []
    odd_count = 0
    impossible = False
    middle_letter = None

    for letter in letters:

        letter_count = txt.count(letter)

        # let's see if there is more than one letter repeated odd times
        if letter_count % 2 != 0:
            if odd_count == 0:
                odd_count += 1
                middle_letter = letter
            else:
                impossible = True
                break

        palindrome.append(letter * (letter_count // 2))

    if impossible:
        return 'impossible'
    else:
        palindrome.sort()
        palindrome_base = ''.join(palindrome)

        return ''.join((
            palindrome_base,
            middle_letter,
            palindrome_base[::-1]
        ))


text = input('Enter the text: ')

print(make_palindrome1(text))  # be my guest - comment this line

# print(make_palindrome2(text))  # and then uncomment this line to try with the second function ;)
