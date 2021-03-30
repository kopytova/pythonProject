from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, option):
        self.option = option

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        Clothes.result += self.calculation + other.calculation
        return Coat(0)

    def __str__(self):
        total = Clothes.result
        Clothes.result = 0
        return f'{total}'


class Coat(Clothes):
    @property
    def calculation(self):
        return round((self.option / 6.5 + 0.5), 1)


class Costume(Clothes):
    @property
    def calculation(self):
        return round(((2 * self.option + 0.3) / 100), 1)

costume = Costume(164)
coat = Coat(42)
print(costume + coat)





