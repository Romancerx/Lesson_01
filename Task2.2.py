# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = list(input("Введите новый элемент: "))  # Create new list
counter = 0  # Just simple counter
print(my_list)  # For comfortable
while counter < len(my_list) - 1:
    my_list[counter], my_list[counter + 1] = my_list[counter + 1], my_list[counter]  # Just like in the lesson)
    counter += 2  # From conditions - 0 <-> 1, 2 <-> 3
print(my_list)
