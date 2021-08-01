"""Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""

array = [[None for g in range(4)] for k in range(4)]

for i in range(4):
    for j in range(4):
        array[i][j] = float(input("Enter number: "))
    (array[i]).append(sum(array[i]))
print(array)
