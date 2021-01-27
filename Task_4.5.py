# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
my_list = list(el for el in range(100, 1001, 2))  # creating list
print(my_list)
print(reduce(lambda prev_el, el: prev_el * el, my_list))  # prev_el - предыдущий элемент, el - текущий элемент

