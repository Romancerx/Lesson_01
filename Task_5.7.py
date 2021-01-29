# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json
# creating vars
firm_profit = 0
average_profit = 0
i = 0
firm_dict = {}
average_dict = {}
all_firms_dict = {}
profit_list = []
# Reading data from file
with open("5.7.txt", "r", encoding="UTF-8") as f:
    for line in f:
        my_list = line.split(" ")  # Creating list with elements
        if int(my_list[2]) - int(my_list[3]) > 0:  # filter firms without profit
            firm_profit = int(my_list[2]) - int(my_list[3])  # count profit
            average_profit += firm_profit  # increase average profit
            i += 1
            firm_dict = {my_list[0]: firm_profit}  # create dict with one firm data
            all_firms_dict.update(firm_dict)  # Add it to global dict
average_profit /= i  # calculating average profit using counter
average_dict = {"average profit": average_profit}  # create average profit dict
profit_list.append(all_firms_dict)  # Create list
profit_list.append(average_dict)
# Write information in json
with open("5.7_file.json", "w") as write_f:
    json.dump(profit_list, write_f)