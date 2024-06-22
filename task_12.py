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
        if isinstance(value, (int, float)):
            self._calories = value
        else:
            print("Калорийность должна быть числом")
            self._calories = None

    def is_healthy(self):
        if isinstance(self._calories, (int, float)):
            return self._calories < 200
        else: return None

    def is_delicious(self):
        return True

    def __str__(self):
        return f"{self._name} Калорийность: {self._calories}, Здоровый {self.is_healthy()}, Вкусный {self.is_delicious()}"



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

jelly_bean = JellyBean('Желе', "sgsdg", 'black licorice')

print(jelly_bean)
print(tiramisu)
