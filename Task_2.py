"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
time_in_seconds = int(input("Введите время в секундах: "))  # Request time in seconds

hours = time_in_seconds // 3600  # Count hours
minutes = time_in_seconds // 60 - hours * 60  # Count minutes
seconds = time_in_seconds % 60  # Count seconds

print(f"Время: {hours}:{minutes}:{seconds}")  # Formatting using "f-strings"
print('Время: %d'':''%d'':''%d' % (hours, minutes, seconds))  # Formatting using "%"
print('Время: {0}:{1}:{2}'.format(hours, minutes, seconds))  # Formatting using ".format"
