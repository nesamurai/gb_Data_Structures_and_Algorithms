"""Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""

def row_sum(n):
    result = 0
    el = 1
    i = 0
    while i < n:
        result = result + el
        el = el * (-0.5)
        i += 1
    return result

elems = int(input("Введите количество элементов для подсчета суммы ряда: "))
print(f'Сумма {elems} элементов ряда равна {row_sum(elems)}')
