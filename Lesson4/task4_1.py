# В качестве алгоритма беру реализацию 5-го задания из 3-го урока.
# Написал вторую реализацию этого алгоритма.

# Я думаю, что сложность первой реализации алгоритма квадратичная,
# потому что при нахождении минимального элемента в массиве осуществляется проход
# по всем элементам массива и также проход по всем элементам осуществляется в
# функции range()

# Я думаю, что сложность второй реализации алгоритма выше, так как
# вначале осуществляется проход по всей индексам массива в функции range(),
# затем проверка наличия элемента среди dictionary с отрицательными элементами,
# и также проход по dictionary с отрицательными элементами, задействованный в
# в функции min() все это возможность дает сложность О(n в кубе)

import cProfile
import random

"""В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве."""

def alg_1(array):
    min_elem = min(array)
    indices = []
    for idx in range(len(array)):
        if array[idx] == min_elem:
            indices.append(idx)

    return "Максимальный отрицательный элемент в массиве '{}' имеет позиции {}".format(min_elem, indices)


# second way to solve algorithm
def alg_2(array):
    negatives = {}
    for idx in range(len(array)):
        num = array[idx]
        if num < 0:
            if num in negatives:
                negatives[num].append(idx)
            else:
                negatives[num] = [idx]
    # print(negatives)
    max_negative = min(negatives)
    return "Максимальный отрицательный элемент в массиве '{}' имеет позиции {}".format(max_negative,
                                                                                    negatives[max_negative])


array_1 = (-22, 12, 0, -90, 88, 88, -90, 0, 12, -22)
array_2 = [random.randint(-100, 100) for num in range(1000000)]


def main_alg_1_1():
    a = alg_1(array_1)

cProfile.run('main_alg_1_1()') # 10 function calls in 0.000 seconds


def main_alg_2_1():
    a = alg_2(array_1)

cProfile.run('main_alg_2_1()') # 10 function calls in 0.000 seconds


def main_alg_1_2():
    a = alg_1(array_2)

cProfile.run('main_alg_1_2()') # 4977 function calls in 0.055 seconds


def main_alg_2_2():
    a = alg_2(array_2)

cProfile.run('main_alg_2_2()') # 497644 function calls in 0.148 seconds
