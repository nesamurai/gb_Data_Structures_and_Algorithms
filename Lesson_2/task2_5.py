"""Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

ten_pairs = ''
for num in range(32, 128):
    if num in (41, 51, 61, 71, 81, 91, 101, 111, 121):
        ten_pairs = ten_pairs + "Num: {} Char: {}\n".format(num, chr(num))
    else:
        ten_pairs = ten_pairs + "Num: {} Char: {} ".format(num, chr(num))
print(ten_pairs)
