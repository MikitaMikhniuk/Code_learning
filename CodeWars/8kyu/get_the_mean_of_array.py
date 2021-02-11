# Get the mean of an array
# https://www.codewars.com/kata/563e320cee5dddcf77000158

# It's the academic year's end, fateful moment of your school report.
# The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

# Return the average of the given array rounded down to its nearest integer.
# The array will never be empty.

def get_average(marks):

    import math

    # marks = [1, 2, 3, 4, 5, 6, 7, 2, 9]
    summ = 0

    for x in marks:
        summ += x
    mean = math.floor((summ / len(marks)))
    return(mean)

marks = [1, 2, 3, 4, 5, 6, 7, 2, 9]
get_average(marks)