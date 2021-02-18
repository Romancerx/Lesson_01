# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
# method init
    def __init__(self, name = "Work", surname = "Hardly", position = "Newbie", income = 50, bonus = None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income, "bonus": bonus}
        if self._income.get("bonus") == None:  # if bonus not transfered, give some consolation
            self._income = {"wage": income, "bonus": 10}

# new class
class Position(Worker):

    def get_full_name(self):  # simple str sum
        full_name = self.name + " " + self.surname
        print(f"Full name : {full_name}")
    def get_total_income(self):  # simple income calculation
        total_income = int(self._income.get("wage")) + int(self._income.get("bonus"))
        print(f"Total income :{total_income}")

worker_1 = Position("Spider","Man", "Defender", 200)
worker_2 = Position("Ant", "Man", "Defender", 150, 100)
# results
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
