#  Пользователь вводит строку из нескольких слов, разделённых пробелами.
#  Вывести каждое слово с новой строки. Строки нужно пронумеровать.
#  Если слово длинное, выводить только первые 10 букв в слове.

user_str = input("Введите фразу: ")  # Create string
my_list = (user_str.split())  # Create list of words from user string
for el in range(0, len(my_list)):
    if len(my_list[el]) < 10:
        print(f"{el.numerator + 1} {my_list[el]}")  # Print word if it lower than 10 letters
    else:
        print(f"{el.numerator + 1} {my_list[el][:10]}")  # Print only 10 letters if word bigger than 10 letters