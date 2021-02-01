# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--wh', type=int)  # working_hours
parser.add_argument('--hp', type=int)  # hour_price
parser.add_argument('--b', type=int, default=None)  # bonus

args = parser.parse_args()
salary = args.wh * args.hp + args.b  # count salary
print(f"Заработная плата сотрудника равна {salary}.")  # print salary

