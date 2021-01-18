# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_str = input("Введите новый элемент: ")
my_list = list(list_str)
print(len(my_list))
counter = 0
print(my_list)
while counter < 19:  # len(list_str):
    my_list[counter], my_list[counter + 1] = my_list[counter + 1], my_list[counter]
    counter += 2
    print(my_list)
