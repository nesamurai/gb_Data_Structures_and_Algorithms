ALPHABET = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
            't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

letter_1 = input("Введите первую букву: ")
letter_2 = input("Введите вторую букву: ")

print("Введенные буквы стоят на местах {0} и {1}, между ними находится {2} букв.".format(ALPHABET[letter_1], ALPHABET[letter_2],
                                                                                    abs(ALPHABET[letter_1] - ALPHABET[letter_2]) - 1))
