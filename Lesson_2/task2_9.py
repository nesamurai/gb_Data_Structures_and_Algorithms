"""Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

number = input("Введите любое натуральное число или пробел для выхода: ")
max_sum = 0

while number != ' ':
    digits_sum = 0
    for digit in number:
        digits_sum += int(digit)
        if digits_sum > max_sum:
            max_sum = digits_sum
            result_num = number
    number = input("Введите любое натуральное число или пробел для выхода: ")
print("Число {} с суммой цифр {} - наибольшее по сумме цифр.".format(result_num, max_sum))
