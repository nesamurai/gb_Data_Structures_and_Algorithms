# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.
import random


array = [round(random.random() * 50, 2) for num in range(21)]
print(f'Исходный массив {array}')

def merge_sort(values):
    if len(values) <= 1:
        return values
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values


sorted_numbers = merge_sort(array)
print(f'Отсортированный по возрастанию массив {sorted_numbers}')

# For example:
# Исходный массив [22.46, 24.58, 29.8, 18.25, 20.35, 13.18, 48.24, 47.8, 37.53, 32.59,
#             6.41, 34.63, 33.98, 12.15, 10.85, 12.5, 39.22, 24.64, 45.04, 19.76, 11.47]
# Отсортированный по возрастанию массив [6.41, 10.85, 11.47, 12.15, 12.5, 13.18, 18.25, 19.76,
#     20.35, 22.46, 24.58, 24.64, 29.8, 32.59, 33.98, 34.63, 37.53, 39.22, 45.04, 47.8, 48.24]
