"""В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

def two_least(array):
    least_elems = [None, None]

    first_min_el = min(array)
    idx_first_min_el = array.index(first_min_el)
    least_elems[0] = array.pop(idx_first_min_el)

    second_min_el = min(array)
    idx_second_min_el = array.index(second_min_el)
    least_elems[1] = array.pop(idx_second_min_el)
    return least_elems


if __name__ == '__main__':
    array1 = [-10, 15, 115, 7, -2, 86, 0, -34, 9, 11]
    array2 = [-34, 15, 115, 7, -21, 86, 0, -34, 9, 11]
    print(two_least(array1))
    print(two_least(array2))
