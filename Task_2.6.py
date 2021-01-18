# *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
#
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

counter = 0
dict_str = ''
my_str = ''
goods_dict = {'title': None,
              'price': None,
              'quantity': None,
              'units': None}

goods_tuple = ()
goods_list = []

title_list = []
price_list = []
quant_list = []
units_list = []
result_dict = {}
while True:
    counter += 1
    if_add_new = input("Add more? ")
    if if_add_new == 'No':
        print(f'List of goods: {goods_list}')
        result_dict = dict(title=title_list,
                           price=price_list,
                           quantity=quant_list,
                           units=units_list)
        print(result_dict)
        break

    my_str = input("Title: ")
    goods_dict['title'] = my_str
    title_list.append(my_str)
    my_str = input("Price: ")
    goods_dict['price'] = my_str
    price_list.append(my_str)
    my_str = input("Quantity: ")
    goods_dict['quantity'] = my_str
    quant_list.append(my_str)
    my_str = (input("Units: "))
    goods_dict['units'] = my_str
    units_list.append(my_str)

    dict_str = goods_dict.copy()
    goods_tuple = (counter, dict_str)
    goods_list.append(goods_tuple)
