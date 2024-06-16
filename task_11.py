class Dessert:
    def __init__(self, name='', calories=0):
        self._name = name
        if isinstance(calories, (int, float)):
            self._calories = calories
        else:
            print("Калорийность должна быть числом")
            self._calories = None

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
        if isinstance(value, (int, float)):
            self._calories = value
        else:
            print("Калорийность должна быть числом")
            self._calories = None

    def is_healthy(self):
        if self._calories is not None:
            return self._calories < 200
        return False

    def is_delicious(self):
        return True


# Пример использования
tiramisu = Dessert('Тирамису', 'sdfs')
waffles = Dessert('Вафли', 192)
print(f'Десерт: {tiramisu.name} Калорийность {tiramisu.calories} Здоровый ли {tiramisu.is_healthy()} Вкусный ли {tiramisu.is_delicious()}')
print(f'Десерт: {waffles.name} Калорийность {waffles.calories} Здоровый ли {waffles.is_healthy()} Вкусный ли {waffles.is_delicious()}')
