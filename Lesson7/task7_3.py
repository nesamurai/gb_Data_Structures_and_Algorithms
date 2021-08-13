# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше медианы.
# Задача решена без сортировки исходного массива.

def mediana(values):
    for val in values:
        left_half = []
        right_half = []
        mediana = val
        array_copy = values[:]
        array_copy.remove(val)
        for num in array_copy:
            if num <= mediana:
                left_half.append(num)
            else:
                right_half.append(num)
        if len(left_half) == len(right_half):
            break
    return mediana


array = [33, 13, -81, -74, -71, -52, 15, -8, -54, -82, 42, -89, 63, -99, -4, -11, 55, 50, -29, -89, 29]
print(sorted(array))
print(mediana(array)) # -11
array_2 = [40, -25, -84, 29, 24, 53, -61, -55, -68, -86, -29, -90, 69, 89, -84, 89, -45, -60, 15, -17, 61]
print(sorted(array_2))
print(mediana(array_2)) # -25
array_3 = [48, -61, -95, 65, 60, -83, 81, 83, -87, 94, 42, -25, 63, 56, -2, -19, 66, 42, 15, 73, 0]
print(sorted(array_3))
print(mediana(array_3)) # 42
