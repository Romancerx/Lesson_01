# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# Open file for reading
my_f = open("out_file.txt", "r", encoding="UTF-8")
lines_counter = 0  # Strings counter

for line in my_f:
    lines_counter += 1
    my_list = line.split(" ")  # Create list of words to find extra spaces

    while my_list.count("") > 0:  # remove extra spaces between words
        my_list.remove("")

    print(f"Количество слов в {lines_counter}-й строке: {len(my_list)}")

my_f.close()  # Close file
print(f"Всего строк: {lines_counter}")

# По идее нужно проверять нет ли между пробелами лишних символов. Я проверил только на лишние пробелы.
# Как красиво проверить на все символы не придумал. Перебирать все ASCII коды сложно, думаю есть простой способ.
