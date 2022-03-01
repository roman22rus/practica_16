class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city
class QuestList(Volunteer):
    def __init__(self,name,city,status):
        super().__init__(name, city)
        self.status = status
    def __str__(self):
        return f'{self.name}, г.{self.city}, статус: {self.status}'

k1= QuestList("Иван Петров", "Москва","Наставник")
k2 = QuestList("Константин Романович","Воронеж","Наставник")
k3 = QuestList("Николай Чернов","Владивосток","Наставник")
print(k1)
print(k2)
print(k3)