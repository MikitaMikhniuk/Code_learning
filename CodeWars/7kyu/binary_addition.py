# Binary Addition
# https://www.codewars.com/kata/551f37452ff852b7bd000139

# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.

def add_binary(a,b):
    x = a+b
    result = ''
    while x > 0:
        result += str(x % 2)
        x //= 2
    return (result [::-1])  # [::-1] - slicing the string form the end to begining

add_binary(51, 12)