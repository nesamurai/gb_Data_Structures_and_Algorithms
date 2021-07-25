num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

for num in (num1, num2, num3):
    if num not in (smallest, largest):
        print("{} является средним числом из трех.".format(num))
