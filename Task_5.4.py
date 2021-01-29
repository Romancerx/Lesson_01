# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def en_ru_trans():  # Use function for read file and change num words
    my_f = open("Count.txt", "r")
    my_string = ""
    for line in my_f:
        result_list = line.split(" ")  # Create list with words

        if result_list[0] == "One":  # Change en words to ru
            result_list[0] = "Один"
        elif result_list[0] == "Two":
            result_list[0] = "Два"
        elif result_list[0] == "Three":
            result_list[0] = "Три"
        elif result_list[0] == "Four":
            result_list[0] = "Четыре"

        my_string += ' '.join(result_list)  # Create new string from list
    my_f.close()  # close file
    return my_string


out_f = open("Count_ru.txt", "w")  # Create file, for writing
out_f.write(en_ru_trans())  # write data
out_f.close()  # close file
# Final commit for pullrequest