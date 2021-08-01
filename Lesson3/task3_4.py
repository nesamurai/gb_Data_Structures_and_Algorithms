"""Определить, какое число в массиве встречается чаще всего."""

array = (1, 2, 3, 4, 4, 4, 3, 2, 1, 1, 2, 4, 1, 2, 2, 3, 3, 4, 1, 2, 3, 4, 4, 2, 2, 1, 2, 1, 2, 3, 1)

unique_nums = sorted(set(array))

most_frequent = 0
for num in unique_nums:
    frequency = array.count(num)
    if frequency > most_frequent:
        most_frequent = frequency
        print(num, most_frequent) # Таким образом напротив числа указана его частотность, если
        # частотность последующего числа выше, то число перезаписывается
