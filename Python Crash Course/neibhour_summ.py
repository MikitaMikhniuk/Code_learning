# Напишите программу, на вход которой подаётся список чисел одной строкой. 
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

# Если на вход пришло только одно число, надо вывести его же.

# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

inputStr = '1 3 5 6 10'
outStr = ''
i = 0

strList = inputStr.split()
for x in strList:
    if i == 0:
        summ = int(strList[i+1]) + int(strList[-1]
        outStr += str(summ)
        i += 1
        summ = 0
    else if i == len(strList) - 1:
        summ = int(strList[i-1]) + int(strList[0]
        outStr += str(summ)
    else:
        summ = int(strList[i-1]) + int(strList[i+1])
        outStr += str(summ)
print(outStr)