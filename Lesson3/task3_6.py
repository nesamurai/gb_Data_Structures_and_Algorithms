"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

def array_sum(array):
    """(list) -> float"""
    min_el = min(array)
    low_idx = array.index(min_el)
    max_el = max(array)
    high_idx = array.index(max_el)

    if low_idx < high_idx:
        result_slice = array[low_idx + 1:high_idx]
    elif low_idx > high_idx:
        result_slice = array[high_idx + 1:low_idx]

    result = 0
    for num in result_slice:
        result += num
    return result


if __name__ == '__main__':
    array1 = (-10.1, -15, 0, 7.7, 17.5, 1, 27, 9.99, 10)
    array2 = (-10, 15, 115, 7, -2.5, 86, -34.45, 9, 11.12)
    print(array_sum(array1))
    print(array_sum(array2))
