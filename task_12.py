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


class JellyBean(Dessert):
    def __init__(self, name='', calories=0, flavor=''):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor != 'black licorice'


tiramisu = Dessert('Тирамису', 300)
waffles = Dessert('Вафли', 192)

jelly_bean = JellyBean('Желе', 50, 'black licorice')

print(
    f'Десерт: {jelly_bean.name} Калорийность {jelly_bean.calories} Здоровый ли {jelly_bean.is_healthy()} Вкусный ли {jelly_bean.is_delicious()} ')
print(
    f'Десерт: {tiramisu.name} Калорийность {tiramisu.calories} Здоровый ли {tiramisu.is_healthy()} Вкусный ли {tiramisu.is_delicious()}')
print(
    f'Десерт: {waffles.name} Калорийность {waffles.calories} Здоровый ли {waffles.is_healthy()} Вкусный ли {waffles.is_delicious()}')
