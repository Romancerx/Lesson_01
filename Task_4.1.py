# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# from argparse import ArgumentParser
#
# parser = ArgumentParser()
#
# parser.add_argument('--work_hours', type=int)
# parser.add_argument('--hour_price', type=int)
# parser.add_argument('--bonus', type=int, default=None)
#
#
# args = parser.parse_args()
# print(f"Заработная плата сотрудника равна {args.work_hours}.")

from sys import argv

#print(f'Our args is {argv}. It is type {type(argv)}, {type(argv[-1])}')
script_name, wh, hp, bonus = argv
print(f'Hello, worker {wh}*{hp}!')
