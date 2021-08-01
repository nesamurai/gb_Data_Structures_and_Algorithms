"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
каждому из чисел в диапазоне от 2 до 9."""

can_divide_by_2 = []
can_divide_by_3 = []
can_divide_by_4 = []
can_divide_by_5 = []
can_divide_by_6 = []
can_divide_by_7 = []
can_divide_by_8 = []
can_divide_by_9 = []

for num in range(2, 100):
    if num % 2 == 0:
        can_divide_by_2.append(num)
    if num % 3 == 0:
        can_divide_by_3.append(num)
    if num % 4 == 0:
        can_divide_by_4.append(num)
    if num % 5 == 0:
        can_divide_by_5.append(num)
    if num % 6 == 0:
        can_divide_by_6.append(num)
    if num % 7 == 0:
        can_divide_by_7.append(num)
    if num % 8 == 0:
        can_divide_by_8.append(num)
    if num % 9 == 0:
        can_divide_by_9.append(num)

print(f'''В диапазоне натуральных чисел от 2 до 99 определено, что:
{len(can_divide_by_2)} чисел кратно 2
{len(can_divide_by_3)} чисел кратно 3
{len(can_divide_by_4)} чисел кратно 4
{len(can_divide_by_5)} чисел кратно 5
{len(can_divide_by_6)} чисел кратно 6
{len(can_divide_by_7)} чисел кратно 7
{len(can_divide_by_8)} чисел кратно 8
{len(can_divide_by_9)} чисел кратно 9''')
