# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

end_flag = 1
result = 0

def find_spaces_func(my_string):
    num = ""
    global end_flag, result
    for el in my_string:
        if el != " " and el != "Q":
            num += el
        elif el == "Q":
            end_flag = 0
            print("break")
            break
        else:
            #print(my_string[len(my_string) - 1])
            result += int(num)
            num = ""
        if el == my_string[len(my_string) - 1]:
            result += int(num)
            num = ""
    print(result)

while end_flag != 0:
    find_spaces_func(input("Введите числа через пробел: "))
