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

# Creating variables, dicts, tuple, lists
counter = 0
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
    if if_add_new == 'No':  # End condition
        print(f'List of goods: {goods_list}')  # Printing our structure
        result_dict = dict(title=title_list,
                           price=price_list,
                           quantity=quant_list,
                           units=units_list)
        print(result_dict)  # Printing result
        break
# Filling dictionary and lists of dict values
    goods_dict['title'] = input("Title: ")
    title_list.append(goods_dict.get('title'))
    goods_dict['price'] = input("Price: ")
    price_list.append(goods_dict.get('price'))
    goods_dict['quantity'] = input("Quantity: ")
    quant_list.append(goods_dict.get('quantity'))
    goods_dict['units'] = (input("Units: "))
    units_list.append(goods_dict.get('units'))
# Creating tuple
    goods_tuple = (counter, goods_dict.copy())
# Adding tuple to list
    goods_list.append(goods_tuple)
