"""Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число."""

# Реализуем в функции первую часть равенства
def nums_sum(natural_number):
    result_1 = 0
    for num in range(natural_number + 1):
        result_1 += num
    return result_1

# Реализуем в функции вторую часть равенства
def formula(natural_number):
    return natural_number * (natural_number + 1) / 2

any_number = int(input("Введите любое натуральное число: "))

# Выполним сравнение двух частей
assert nums_sum(any_number) == formula(any_number), "Что-то не то!"
