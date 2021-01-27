# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# Using factorial in math module
from math import factorial
# factorial count function
def fact(n):
    for i in range(1, n+1):  # Count factorials for all in 1! to n!
        yield factorial(i)  # factorials generator
n = int(input("Введите число, для вычисления факторила: "))
for el in fact(n):
    print(el)
