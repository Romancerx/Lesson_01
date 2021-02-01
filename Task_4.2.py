# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random  # Using random library

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # Creating original list
print(f"Исходный список: {original_list}")

my_list = []  # Generating random list
for el in original_list:
    my_list.append(el + random.randrange(1, 1000, 1))  # Using random for creativity
print(f"Сгенерированный список: {my_list}")

result_list = []
for i in range(0, len(my_list)-1):  # Finding goal elements and creating result list
    if my_list[i+1] > my_list[i]:
        result_list.append(my_list[i+1])
print(f"Результат: {result_list}")
