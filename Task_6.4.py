# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

# class Car
class Car:
    # default vars
    speed = 0
    color = "red"
    name = "VAZ"
    is_police = False

# magic init
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

# define methods with simple prints
    def go(self):
        print(f"{self.name} поехала")
    def stop(self):
        print(f"{self.name} остановилась")
    def turn(self, direction):
        print(f"{self.name} повернула {direction}")
    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed} км/ч")

class TownCar(Car):  # towncar with redefined method
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} км/ч")
        print(f"Текущая скорость {self.name} {self.speed}")

class SportCar(Car):
    pass  # Nothing in task conditions

class WorkCar(Car):  # workcar with redefined method
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} км/ч")
        print(f"Текущая скорость {self.name} {self.speed}")

class PoliceCar(Car):
    is_police = True  # policecar with redefined attribute

# result
police_car = PoliceCar(70, "white", "ferrari")
print(police_car.color, police_car.speed, police_car.name, police_car.is_police)
police_car.go()
police_car.stop()
police_car.turn("налево")
police_car.show_speed()
print("*********")
traffic_car = WorkCar(41, "black", "UAZ")
print(traffic_car.color, traffic_car.speed, traffic_car.name, traffic_car.is_police)
traffic_car.go()
traffic_car.stop()
traffic_car.turn("направо")
traffic_car.show_speed()
print("*********")
sport_car = SportCar(150, "Yellow", "Camaro")
print(sport_car.color, sport_car.speed, sport_car.name, sport_car.is_police)
sport_car.go()
sport_car.stop()
sport_car.turn("налево")
sport_car.show_speed()
print("*********")
town_car = TownCar(67, "Green", "Smart")
print(town_car.color, town_car.speed, town_car.name, town_car.is_police)
town_car.go()
town_car.stop()
town_car.turn("направо")
town_car.show_speed()