# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить её на экран.

with open("5.5_file.txt", "w") as out_f:# Create file, for writing
    out_f.write(input("Введите числа через пробел: "))  # add numbers string

with open("5.5_file.txt", "r") as my_f:# Open file for reading
    my_string = my_f.read()  # read data

my_list = my_string.split()  # Collecting data to list for easily calculating
my_sum = 0
for i in range(0, len(my_list)):
    if my_list[i].isdigit():  # chek for nondigit symbol
        my_sum += int(my_list[i])  # calculating
    else:
        print(f"Ошибка, {my_list[i]} не цифра")  # if error, just print message and continue calculating

print(my_sum)  # print result