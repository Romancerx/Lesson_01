# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# sipmle class
class Stationery():
    title = "канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки")
# sipmle class
class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")
# sipmle class
class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")
# sipmle class
class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")
# results
stationery = Stationery()
stationery.draw()
print("********")
pen = Pen()
pen.draw()
print("********")
pencil = Pencil()
pencil.draw()
print("********")
handle = Handle()
handle.draw()