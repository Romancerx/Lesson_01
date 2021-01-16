#1. Поработайте с переменными,
#a) создайте несколько, выведите на экран,
#б) запросите у пользователя несколько чисел и строк, сохраните в переменные,
#в) выведите на экран.

#a) Creating new variables
number = 0
number_float = 2.14
string = "Hello!"

error_flag_1 = 0 # Используем для проверки ввода правильного типа данных
error_flag_2 = 0 # Используем для проверки ввода правильного типа данных
error_flag_3 = 0 # Используем для проверки ввода правильного типа данных

#print new variables
print(number, number_float, string)

#б) request some numbers and strings

"""
Ввод строкового значения при запросе числа выдает ошибку.
По идее нужно проверять, что ввели. 

без проверки:
user_number1 = int(input("Введите первое число: "))
user_number2 = int(input("Введите второе число: "))
user_number3 = int(input("Введите третье число: "))
"""
# C проверкой (уверен можно сделать код короче, но мне не хватает времени додумать):
while error_flag_1 == 0:
    try:
        user_number1 = int(input("Введите первое число: "))
        error_flag_1 = 1
    except:
        print('Введено "неправильное" число')

while error_flag_2 == 0:
    try:
        user_number2 = int(input("Введите второе число: "))
        error_flag_2 = 1
    except:
        print('Введено "неправильное" число')

while error_flag_3 == 0:
    try:
        user_number3 = int(input("Введите третье число: "))
        error_flag_3 = 1
    except:
        print('Введено "неправильное" число')

user_string1 = input("Введите текст: ")
user_string2 = input("Введите еще немного букоф: ")
user_string3 = input("Введите и еще пару слов : ")

#в) Print

print("Введенные числа \n", user_number1, user_number2, user_number3)
print("Введенные строки \n", user_string1, "\n", user_string2, "\n", user_string3)

# Почему "\n" вводит пробел или отступ в начале строки???
# Commit






