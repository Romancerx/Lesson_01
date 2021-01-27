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

from itertools import count, cycle
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--start', type=int)  #
parser.add_argument('--stop_count', type=int)  #
parser.add_argument('--stop_cycle', type=int, default=10)  #
args = parser.parse_args()

my_list = []

for el in count(args.start):
    if el > args.stop_count:
        break
    else:
        my_list.append(str(el))
print(my_list)

my_list = []
с = 0
for el in cycle("ABC"):
    if с > args.stop_cycle:
        break
    my_list.append(el)
    с += 1
print(my_list)

