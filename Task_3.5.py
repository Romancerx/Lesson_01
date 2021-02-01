# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# global vars
end_flag = 1
result = 0


def find_spaces_func(my_string):
    num = ""  # Clear "num" var
    global end_flag, result

    for i in range(0, len(my_string)):
        if my_string[i] != " " and my_string[i] != "Q":  # Find spaces and char Q
            num += my_string[i]  # Add symbols before space found
        elif my_string[i] == "Q":  # Exit if Q symbol found
            end_flag = 0  # Flag for stop programm
            break
        else:
            result += int(num)  # Sum numbers
            num = ""  # Clean old number
        if i == len(my_string) - 1:  # Adding last symbol
            result += int(num)
            num = ""
    print(f"Сумма всех чисел равна: {result}")


while end_flag != 0:
    find_spaces_func(input("Введите числа через пробел, символ Q для выхода: "))
