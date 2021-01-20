# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# Collecting data)
earn = int(input("Введите размер выручки: "))
costs = int(input("Введите размер издержек: "))

# figure out our situation
if earn > costs:
    print(f"Финансовый результат - прибыль")
    profit = earn - costs
    print(f"Рентабельность выручки = {profit / earn}")
    people = int(input("Введите численность сотрудников фирмы: " ))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {profit / people}")
elif earn < costs:
    print(f"Финансовый результат - убыток")
else:
    print(f"Финансовый результат - прибыль равна выручке")

# Commit