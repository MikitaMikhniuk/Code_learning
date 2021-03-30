# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел.

# Используйте метод split строки. 

str = input()
summ = 0

strList = str.split()
for x in strList:
    summ += int(x)
print(summ)