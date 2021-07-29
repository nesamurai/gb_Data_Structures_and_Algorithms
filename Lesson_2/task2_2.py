"""Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

natural = input("Введите натуральное число: ")
amount_even = 0
amount_odd = 0
digits_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for digit in natural:
    digits_dict[digit] += 1

amount_even = digits_dict['0'] + digits_dict['2'] + digits_dict['4'] + digits_dict['6'] + digits_dict['8']
amount_odd = digits_dict['1'] + digits_dict['3'] + digits_dict['5'] + digits_dict['7'] + digits_dict['9']
print("В введенном числе {} четных цифр.".format(amount_even))
print("В введенном числе {} нечетных цифр.".format(amount_odd))
