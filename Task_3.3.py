# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# creating function and use list for usability)))
def my_func(arg_1, arg_2, arg_3):
    my_list = (arg_1, arg_2, arg_3)
    return sum(my_list) - min(my_list)
# Ask to put numbers
user_arg1 = int(input("Введите 1-е число: "))
user_arg2 = int(input("Введите 2-е число: "))
user_arg3 = int(input("Введите 3-е число: "))
# print result
print(my_func(user_arg1, user_arg2, user_arg3))
