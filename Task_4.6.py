# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

# Using modules and functions
from itertools import count, cycle
from argparse import ArgumentParser

# creating parameters for script
parser = ArgumentParser()

parser.add_argument('--start', type=int)  # "count" function start position
parser.add_argument('--stop_count', type=int)  # "count" function stop position
parser.add_argument('--stop_cycle', type=int, default=10)  # "cycle" function stop iteration parameter
args = parser.parse_args()

my_list = []  # creating list for friendly print:)

# cycle for count section
for el in count(args.start):
    if el > args.stop_count:
        break
    else:
        my_list.append(str(el))  # append elements to list
print(my_list)

my_list = []  # clear list
с = 0  # use counter
# cycle for cycle section
for el in cycle("ABC"):
    if с > args.stop_cycle:
        break
    my_list.append(el)  # append elements to list
    с += 1
print(my_list)

