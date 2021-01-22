# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# input args
x_arg = int(input("Введите действительное положительное число(x): "))
y_arg = int(input("Введите целое отрицательное число(y): "))

# simple func with '**' use
def my_func(x, y):
    return x ** y

# func without using '**'
def my_func2(x, y):
    z = 1
    for i in range(0, abs(y)):
        z *= x
    return 1 / z

# print results
print(my_func(x_arg, y_arg))
print(my_func2(x_arg, y_arg))

