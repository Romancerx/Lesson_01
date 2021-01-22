# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# input strings
user_name = input("Введите имя пользователя: ")
user_surname = input("Введите фамилию пользователя: ")
user_yob = int(input("Введите год рождения пользователя: "))
user_city_living = input("Введите город проживания пользователя: ")
user_email = input("Введите email пользователя: ")
user_phone = input("Введите телефон пользователя: ")

# simple function
def user_info(name, surname, year_of_birth,  city_living, email=None, phone=None):
    print(f'Информация о пользователе: {name}, {surname}, {year_of_birth}, {city_living}, {email}, {phone}')

# named args?
user_info(name=user_name,
          surname=user_surname,
          year_of_birth=user_yob,
          city_living=user_city_living,
          email=user_email,
          phone=user_phone)
