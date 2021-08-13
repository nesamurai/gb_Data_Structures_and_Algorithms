"""Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

sequence_quantity = int(input("Введите количество чисел: "))
digit = input("Введите цифру: ")

sequence = ''
while sequence_quantity > 0:
    num = input("Введите поочереди числа последовательности: ")
    sequence += num
    sequence_quantity -= 1
print(f'Ваша последовательность {sequence}')

amount = 0
for i in sequence:
    if i == digit:
        amount += 1

print("В введенной последовательности чисел цифра {} встречается {} раз.".format(digit, amount))
