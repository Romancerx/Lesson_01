# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Request some number
user_number = int(input("Введите число: "))
# Formatting "nn" and "nnn"
nn = '%d''%d' % (user_number, user_number)
nnn = '%d''%d''%d' % (user_number, user_number, user_number)
# Printing result
print(int(user_number) + int(nn) + int(nnn))

# Print in one string
print(int(user_number)
      + int('%d''%d' % (user_number, user_number))
      + int('%d''%d''%d' % (user_number, user_number, user_number)))

# Commit