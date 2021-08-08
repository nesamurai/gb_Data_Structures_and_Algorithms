# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
NUMBERS_16 = {val: key for key, val in NUMBERS.items()}

collection_1 = list(input("Введите первое шестнадцатеричное число: "))
collection_2 = list(input("Введите второе шестнадцатеричное число: "))


def sum_and_product(collection_1, collection_2):
    reverse_1 = collection_1[::-1]
    reverse_2 = collection_2[::-1]
    # Перевод чисел в десятичное представление
    value_1 = 0
    for idx in range(len(reverse_1)):
        value_1 += NUMBERS[reverse_1[idx]] * pow(16, idx)

    value_2 = 0
    for idx in range(len(reverse_2)):
        value_2 += NUMBERS[reverse_2[idx]] * pow(16, idx)

    summation = value_1 + value_2
    product = value_1 * value_2

    sum_degree = 0
    while summation > pow(16, sum_degree):
        sum_degree += 1

    sum_result = []
    while sum_degree > 0:
        sum_result.append(summation // pow(16, sum_degree-1))
        summation = summation % pow(16, sum_degree-1)
        sum_degree -= 1

    summation_16 = ''
    for elem in sum_result:
        summation_16 += NUMBERS_16[elem]

    # вычисление произведения аналогично вычислению суммы
    prod_degree = 0
    while product > pow(16, prod_degree):
        prod_degree += 1

    prod_result = []
    while prod_degree > 0:
        prod_result.append(product // pow(16, prod_degree-1))
        product = product % pow(16, prod_degree-1)
        prod_degree -= 1

    product_16 = ''
    for elem in prod_result:
        product_16 += NUMBERS_16[elem]

    # print(summation_16, product_16)
    return summation_16, product_16

sum_and_product(collection_1, collection_2)
