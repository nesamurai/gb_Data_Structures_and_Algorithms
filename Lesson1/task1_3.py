def equasion():
    x1 = int(input("Введите координату Х первой точки: "))
    y1 = int(input("Введите координату Y первой точки: "))
    x2 = int(input("Введите координату Х второй точки: "))
    y2 = int(input("Введите координату Y второй точки: "))

    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1

    return "y = {}x + {}".format(k, b)


print(equasion())
