num_xxx = int(input("Введите трехзначное число: "))

def operations(num):
    hundreds = num // 100
    tens = (num - hundreds * 100) // 10
    ones = num - hundreds * 100 - tens * 10
    their_sum = hundreds + tens + ones
    their_product = hundreds * tens * ones
    return their_sum, their_product

print(operations(num_xxx))
