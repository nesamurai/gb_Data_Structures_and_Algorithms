def substrings_amount(word):
    result = []
    for idx in range(len(word)):
        word_part = word[idx:]
        idx = len(word_part) - 1
        while idx >= 0:
            if word_part[:idx + 1] != word:
                result.append(word_part[:idx + 1])
            idx -= 1
    print(result)
    return len(result)

print(substrings_amount('sock'))
print(substrings_amount('algorithm'))
