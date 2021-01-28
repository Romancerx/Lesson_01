# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_f = open("salary.txt", "r", encoding="UTF-8")
workers_count = 0
all_sal = 0
for line in my_f:
    workers_count += 1
    my_list = line.split(" ")
    if int(my_list[1]) < 20000:
        print(my_list[0])
    all_sal += int(my_list[1])

my_f.close()  # Close file
print(f"Средний уровень зарплаты: {all_sal / workers_count}")
