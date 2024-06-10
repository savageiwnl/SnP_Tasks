class Dessert:
    def __init__(self, name='', calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True


tiramisu = Dessert('Тирамису', 300)
waffles = Dessert('Вафли', 192)

print(
    f'Десерт: {tiramisu.name} Калорийность {tiramisu.calories} Здоровый ли {tiramisu.is_healthy()} Вкусный ли {tiramisu.is_delicious()}')
print(
    f'Десерт: {waffles.name} Калорийность {waffles.calories} Здоровый ли {waffles.is_healthy()} Вкусный ли {waffles.is_delicious()}')
