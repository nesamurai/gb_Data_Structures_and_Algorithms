# Написать два алгоритма нахождения i-го по счёту простого числа.
import cProfile

# - Без использования Решета Эратосфена

# Я думаю, что сложность данного алгоритма O(n), так как проход по элементам
# осуществляется в одном цикле, где идет проверка на наличие остатка от деления
# на уже имеющиеся простые числа

def eratosfen(i):
    simple_num  = 2
    simple_nums = [simple_num]
    if i == 1:
        return simple_num
    else:
        simple_num += 1
        while len(simple_nums) < i:
            for num in simple_nums:
                if simple_num % num == 0:
                    break
            else:
                simple_nums.append(simple_num)
            simple_num += 1
    return simple_nums[-1]


def first():
    a = 1000
    s = eratosfen(a)

def second():
    b = 10000
    t = eratosfen(b)

cProfile.run('first()') # 8922 function calls in 0.020 seconds
cProfile.run('second()') # 114732 function calls in 1.846 seconds


# - Использовать алгоритм решето Эратосфена

# Я думаю, что сложность предложенного в методичке алгоритма квадратичная, так как
# осуществляется два прохода по всем числам: вначале цикл for заполнения массива,
# далее while (там так и указано).

# n = int(input("вывод простых чисел до числа ... "))
def default_eratosfen(n):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0

    m = 2
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


def first_default():
    a = 1000
    s = default_eratosfen(a)

def second_default():
    b = 10000
    t = default_eratosfen(b)

cProfile.run('first_default()') # 173 function calls in 0.000 seconds
cProfile.run('second_default()') # 1234 function calls in 0.003 seconds
