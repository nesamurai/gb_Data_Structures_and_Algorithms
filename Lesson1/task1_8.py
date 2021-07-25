def long_year():
    num = int(input("Введите год: "))
    if num % 400 == 0:
        return f'{num} - високосный год'
    elif num % 100 == 0:
        return f'{num} - невисокосный год'
    elif num % 4 == 0:
        return f'{num} - високосный год'
    else:
        return f'{num} - невисокосный год'
