"""В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве."""

array = (-22, 12, 0, -90, 88, 88, -90, 0, 12, -22)

min_elem = min(array)
indices = []
for idx in range(len(array)):
    if array[idx] == min_elem:
        indices.append(idx)

print("Максимальный отрицательный элемент в массиве '{}' имеет позиции {}".format(min_elem, indices))
