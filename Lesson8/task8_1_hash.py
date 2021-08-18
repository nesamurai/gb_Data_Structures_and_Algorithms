# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def substrings_amount(word):
    result = []
    word_hash = hashlib.sha1(word.encode('utf-8')).hexdigest()
    for idx in range(len(word)):
        word_part = word[idx:]
        word_part_hash = hashlib.sha1(word_part.encode('utf-8')).hexdigest()
        idx = len(word_part) - 1
        while idx >= 0:
            indexed_word_part_hash = hashlib.sha1(word_part[:idx + 1].encode('utf-8')).hexdigest()
            if indexed_word_part_hash != word_hash:
                result.append(word_part[:idx + 1])
            idx -= 1
    return len(result)

print(substrings_amount('sock'))
print(substrings_amount('algorithm'))
