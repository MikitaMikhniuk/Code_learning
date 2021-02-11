# Is this a triangle?
# https://www.codewars.com/kata/56606694ec01347ce800001b

# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    if (a + b > c or b + c > a or a + c > b):
        return True
    elif (a and b and c <= 0):
        return False
    else:
        return False

is_triangle(7, 2, 2)