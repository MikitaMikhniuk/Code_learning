# Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    for x in input_str:
        if (x == 'a') or (x == 'e') or (x == 'i') or (x == 'o') or (x == 'u'):
            num_vowels += 1
        else:
            continue
    return num_vowels

print(get_count('Hello'))

