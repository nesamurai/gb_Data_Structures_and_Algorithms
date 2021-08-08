# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
# ниже среднего.

amount = int(input("Enter the quantity of enterprises: "))

enterprises = [{} for x in range(amount)]

for enterprise in enterprises:
    enterprise['name'] = input("Enter the name of the {} enterprise: ".format(enterprises.index(enterprise) + 1))
    enterprise['profit_1'] = int(input("Enter the first quarter profit \
of the {} enterprise: ".format(enterprises.index(enterprise) + 1)))
    enterprise['profit_2'] = int(input("Enter the second quarter profit \
of the {} enterprise: ".format(enterprises.index(enterprise) + 1)))
    enterprise['profit_3'] = int(input("Enter the third quarter profit of \
the {} enterprise: ".format(enterprises.index(enterprise) + 1)))
    enterprise['profit_4'] = int(input("Enter the fourth quarter profit of \
the {} enterprise: ".format(enterprises.index(enterprise) + 1)))

for enterprise in enterprises:
    enterprise['year_profit'] = enterprise['profit_1'] + enterprise['profit_2'] + enterprise['profit_3'] + enterprise['profit_4']

print(enterprises)

total_profit = 0
for enterprise in enterprises:
    total_profit += enterprise['year_profit']

average_profit = total_profit / amount
print(f"Средняя прибыль за год для всех предприятий составляет {average_profit}")

big_profit = ''
little_profit = ''
medium_profit = ''
for enterprise in enterprises:
    if enterprise['year_profit'] > average_profit:
        big_profit += enterprise['name'] + ' '
    elif enterprise['year_profit'] < average_profit:
        little_profit += enterprise['name'] + ' '
    else:
        medium_profit += enterprise['name'] + ' '

print("Предприятия {} имеют прибыль выше среднего, \
предприятия {} имеют прибыль ниже среднего.".format(big_profit.rstrip(), little_profit.rstrip()))
