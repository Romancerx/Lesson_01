# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Request some number
user_number = input("Введите целое, положительное число: ")

counter = 0  # Create counter
max_digit = 0  # Create variable. It will be max digit.

while counter < len(user_number):  # Перебираем в цикле все цифры
    if max_digit < int(user_number[counter]):  # Compare max_digit with next digit in user_number
        max_digit = int(user_number[counter])
        counter += 1  # Increment counter by 1
    else:
        counter += 1  # Increment counter by 1

# Printing answer
print(f"Самая большая цифра в числе {user_number} - {max_digit}")
