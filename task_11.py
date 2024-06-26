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
        if isinstance(self._calories, (int, float)):
            return self._calories < 200
        else:
            return 'не определить'

    def is_delicious(self):
        return True

    def __str__(self):
        return f"{self._name} Калорийность: {self._calories}, Здоровый десерт {self.is_healthy()}, Вкусный десерт {self.is_delicious()}"


# Пример использования
tiramisu = Dessert('Тирамису', "100ff")  # Калорийность задана строкой
print(tiramisu)  # Выведет: Тирамису (Калорийность: 200.0)
