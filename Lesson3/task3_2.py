"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа."""

def even_elems_indices(first_list):
    """(list) => list
    Returns list with indices of even elements of provided list.
    """
    second_list = []
    for idx in range(len(first_list)):
        if first_list[idx] % 2 == 0:
            second_list.append(idx)
    return second_list

print(even_elems_indices([8, 3, 15, 6, 4, 2]))
print(even_elems_indices([8, 3, 15, 6, 4, 2, 2, 4, 6, 15, 3, 8]))
print(even_elems_indices([8, 8, 8, 8, 8]))
print(even_elems_indices([0, 0, 0, 0]))
print(even_elems_indices([1, 1, 1, 1, 1, 1]))
