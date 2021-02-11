# Square(n) Sum
# https://www.codewars.com/kata/515e271a311df0350d00000f

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    summ = 0
    for x in numbers:
        summ += x ** 2
    return(summ)

numbers = []
square_sum(numbers)