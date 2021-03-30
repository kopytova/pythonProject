class Cell:

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.num // row)]) + '\n' + '*' * (self.num % row)

    def __str__(self):
        return f'{self.num}'

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print('Сумма клеток равна: ')
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print('Разность двух клеток равна: ')
        return Cell(self.num - other.num) if self.num - other.num > 0 \
            else 'В первой клетке недостаточно ячеек для операции'

    def __mul__(self, other):
        print('Произведение двух клеток равно: ')
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print('Частное двух клеток равно: ')
        return Cell(self.num // other.num)

cell_1 = Cell(220)
cell_2 = Cell(13)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)