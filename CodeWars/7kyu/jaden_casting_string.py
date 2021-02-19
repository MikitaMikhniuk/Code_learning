# Jaden Casing Strings
# https://www.codewars.com/kata/5390bac347d09b7da40006f6


# def to_jaden_case(string):
string = "How can mirrors be real if our eyes aren't real"
x = string.split()
str = ''
for y in x:
    str += y.capitalize() + ' '
print(str.strip())