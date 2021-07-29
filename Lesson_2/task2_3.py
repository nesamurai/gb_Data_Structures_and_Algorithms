"""Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843."""

number = input("Введите число: ")
n = len(number) - 1
reversed_number = ''
while n >= 0:
    reversed_number += number[n]
    n -= 1
print(reversed_number)
