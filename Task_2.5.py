# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_str = ''  # Create empty string for good-looking answer
rating = [25, 13, 8, 4, 2, 2, 1]  # Our structure
new_rate = int(input("Введите новый рейтинг: "))
# If we already have same ratings, insert new after old
if rating.count(new_rate) > 0:
    rating.insert(rating.index(new_rate) + rating.count(new_rate), new_rate)
# If we haven't got same ratings, just add new one, and sort list)
else:
    rating.append(new_rate)
    rating.sort()
    rating.reverse()
# Result like in example. We can also write "print(rating)", but there are "[]" will be in the answer
for el in range(0, len(rating)):
    my_str += ', ' + str(rating[el])
print(f"{my_str[2:]}.")
