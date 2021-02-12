# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, _length = 20, _width = 5000):  # magic method with default values
        self._length = _length
        self._width = _width

    def asphalt_weight(self):  # input weight and depth of asphault and calculating
        m_weight = int(input("Введите массу асфальта для покрытия 1-го кв метра дороги: "))
        depth = int(input("Введите толщину асфальта: "))
        asph_w = self._length * self._width * m_weight * depth
        print (f"{self._length}м * {self._width}м * {m_weight}кг * {depth}см = {int(asph_w / 1000)} т")


# result:
my_road = Road(20, 5000)
my_road.asphalt_weight()