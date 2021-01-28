# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

out_f = open("new_file.txt", "w")  # Create file, for writing
while True:
    user_str = input("Введите строку: ")
    if user_str == "":  # stop condition
        break
    out_f.write(user_str + "\n")  # add new string
out_f.close()  # close file
