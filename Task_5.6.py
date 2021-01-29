# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# Vars
my_list = []
my_dict = {}
result_dict = {}
my_str = ""
value = 0
# Open file for reading
with open("5.6.txt", "r", encoding="UTF-8") as f:
    for line in f:
        my_list = line.split(" ")  # Creating list with elements
        for i in range(1, len(my_list)):
            if my_list[i] != chr(8212) and my_list[i] != chr(8212)+"\n":  # Find only numbers. Text have strange symbols "-". Skip it.
                value += int(my_list[i].split("(")[0])  # Calculating hours.
        my_str = my_list[0]  # Create string var for use it instead of key.
        my_dict = {my_str[:len(my_str) - 1]: value}  # Create new dict with one lesson name
        result_dict.update(my_dict)  # Generating result dict with all lessons
        value = 0  # Clear hours before next lesson reading

print(result_dict)