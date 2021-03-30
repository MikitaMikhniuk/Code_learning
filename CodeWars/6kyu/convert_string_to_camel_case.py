# https://www.codewars.com/kata/517abf86da9663f1d2000003

# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# function toCamelCase(str){
str = 'the_stealth_warrior'
outStr = ''

for x in str:
    if x == '-':
        splitStr = str.split('-')
        break
    elif x == '_':
        splitStr = str.split('_') 
for y in splitStr:
    if y != y.capitalize():
        outStr += y.capitalize()
    elif y:
        outStr += y
print(outStr)