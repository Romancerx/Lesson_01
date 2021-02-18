# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time, sys  # import

class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]  # create attribute

    def running(self):  # Method with correct order
        print(self.__color[0])
        time.sleep(7)
        print(self.__color[1])
        time.sleep(2)
        print(self.__color[2])
        time.sleep(7)

my_tl = TrafficLight()  # new copy of class
while True:
    try:
        my_tl.running()  # start running method
    except KeyboardInterrupt:  # decide to use built-in keyboard interrupt class
        sys.exit()  # exit when "ctrl+c" is pressed (working only in terminal)
