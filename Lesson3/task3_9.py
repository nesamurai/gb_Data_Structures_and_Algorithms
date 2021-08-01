"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

example_matrix = [
            [1.0, 25.0, 3.3, 8.0, 66.6],
            [9.6, 65.0, -72.2, -5.0, -2.9],
            [9.9, -35, 15.0, 12.22, -78.0],
            [-52.25, 100.0, 0.0, -3.4, 87.65],
            [20.7, -13.1, -28.6, 28.3, 29.5]
]


def max_in_matrix_min_elems(matrix):
    columns_elems = []
    for i in range(len(matrix[0])): # row
        lst = []
        for j in range(len(matrix)):
            lst.append(matrix[j][i])
        columns_elems.append(lst)
    print(columns_elems)

    columns_min_elems = [min(inner) for inner in columns_elems]
    print(columns_min_elems)

    max_in_min_elems = max(columns_min_elems)
    return max_in_min_elems


print(max_in_matrix_min_elems(example_matrix))
