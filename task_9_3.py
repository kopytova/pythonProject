class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):


    def get_full_name(self):
        return f'{self.name} {self.surname}'


    def get_total_income(self):
        total = sum(self._income.values())
        return total


employee = Position('Иван', 'Петров', 'Администратор', 40000, 15000)
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())


