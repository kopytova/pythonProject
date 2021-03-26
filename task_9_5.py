class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашем {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером {self.title}')

s = Stationery('с использованием разных вариантов')
s.draw()

pn = Pen('Delucci')
pn.draw()

pl = Pencil('Stabilo')
pl.draw()

h = Handle('Maped')
h.draw()
