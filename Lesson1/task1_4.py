import random


a = int(input('Введите левую границу для искомого целого числа: '))
b = int(input('Введите правую границу для искомого целого числа: '))

int_num = random.randint(a, b)
print(int_num)


c = float(input('Введите левую границу для искомого вещественного числа: '))
d = float(input('Введите правую границу для искомого вещественного числа: '))

float_num = random.uniform(c, d)
print(float_num)


ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z')

letter1 = input('Введите левую границу для искомого символа: ')
letter2 = input('Введите правую границу для искомого символа: ')


def random_symbol(left_bound, right_bound):
    num_of_symbol_1 = ord(left_bound)
    num_of_symbol_2 = ord(right_bound)
    rand_num_for_symbol = random.randint(num_of_symbol_1, num_of_symbol_2)
    return chr(rand_num_for_symbol)


print(random_symbol(letter1, letter2))
