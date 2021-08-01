"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random


random_list = []
for _ in range(10):
    random_list.append(random.randint(1, 1000))
print(random_list)


# Нахожу максимальный элемент списка и его индекс
max_elem = max(random_list)
max_el_idx = random_list.index(max_elem)
# Нахожу минимальный элемент списка и его индекс
min_elem = min(random_list)
min_el_idx = random_list.index(min_elem)

final_list = []
if max_el_idx < min_el_idx:
    final_list = random_list[:max_el_idx] + [random_list[min_el_idx]] + \
    random_list[max_el_idx + 1:min_el_idx] + [random_list[max_el_idx]] + \
    random_list[min_el_idx + 1:]
elif max_el_idx > min_el_idx:
    final_list = random_list[:min_el_idx] + [random_list[max_el_idx]] + \
    random_list[min_el_idx + 1:max_el_idx] + [random_list[min_el_idx]] + \
    random_list[max_el_idx + 1:]
print(final_list)
