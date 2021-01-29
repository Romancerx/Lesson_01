# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить её на экран.

out_f = open("5.5_file.txt", "w")  # Create file, for writing
user_str = input("Введите числа через пробел: ")
out_f.write(user_str)  # add new string
out_f.close()  # close file

my_f = open("5.5_file.txt", "r", encoding="UTF-8")
my_string = my_f.read()
my_f.close()
my_list = my_string.split()
my_sum = 0
for i in range(0, len(my_list)):
    my_sum += int(my_list[i])
    
print (my_sum)
