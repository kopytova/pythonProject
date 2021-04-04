def get_answer(*valid_answers, question="Выберите пункт меню"):
    print()
    while True:
        try:
            answer = int(input(f"{question}: "))
            if answer in valid_answers:
                return answer
        except ValueError:
            pass


class Stock:
    def __init__(self, *departments):
        self.equipments = list()
        self.department = dict()
        for d in departments:
            self.department[d] = list()

    def add_equipment(self):
        print("Класс оргтехники:\n")
        print("\t1. Принтер")
        print("\t2. Сканер")
        print("\t3. Ксерокс")
        answer = get_answer(1, 2, 3)
        if answer == 1:
            self.equipments.append(Printer.create())
        elif answer == 2:
            self.equipments.append(Scanner.create())
        elif answer == 3:
            self.equipments.append(Xerox.create())

    def show_departments(self):
        departments = self.department.keys()
        for i, department in enumerate(departments):
            print(f"{i}. {department}")
        return tuple(departments)

    def move_equipment(self):
        self.show_equipments(no_departments=True)
        e_index = get_answer(*range(len(self.equipments)), question="ID оборудования")
        print()

        departments = self.show_departments()
        d_index = get_answer(*range(len(departments)), question="ID департамента")
        d_key = departments[d_index]
        print()

        self.department[d_key].append(self.equipments.pop(e_index))
        print("Перемещение выполнено\n")

    def show_equipments(self, no_departments=False):
        print("*" * 40)
        print("* На складе: ")
        print("*" * 40)
        print()
        for i, e in enumerate(self.equipments):
            print(f"# ID: {i}")
            print(e)
            print()
        if no_departments: return

        for d in self.department.keys():
            print("*" * 40)
            print("*" + d)
            print("*" * 40)
            print()
            for i, e in enumerate(self.department[d]):
                print(f"# ID: {i}")
                print(e)
                print()


class Equipment:
    def __init__(self, ename, vendor, model, serial):
        self.ename, self.vendor, self.model, self.serial = ename, vendor, model, serial

    @staticmethod
    def create():
        vendor = input("Производитель: ")
        model = input("Модель устройства: ")
        serial = input("Серийный номер: ")
        return vendor, model, serial

    def __str__(self):
        return f"Тип устройства: {self.ename}\nПроизводитель: {self.vendor}\nМодель устройства: {self.model}\nСерийный номер: {self.serial}"


class Printer(Equipment):
    def __init__(self, vendor, model, serial, ptype):
        super().__init__("Принтер", vendor, model, serial)
        self.ptype = ptype

    def __str__(self):
        return super().__str__() + f"\nТип принтера: {self.ptype}"

    @classmethod
    def create(cls):
        vendor, model, serial = super().create()
        ptype = input("Тип принтера: ")
        return cls(vendor, model, serial, ptype)


class Scanner(Equipment):
    def __init__(self, vendor, model, serial, dpi):
        super().__init__("Сканер", vendor, model, serial)
        self.dpi = dpi

    def __str__(self):
        return super().__str__() + f"\nКоличество точек на дюйм: {self.dpi}"

    @classmethod
    def create(cls):
        vendor, model, serial = super().create()
        dpi = input("Количество точек на дюйм: ")
        return cls(vendor, model, serial, dpi)


class Xerox(Equipment):
    def __init__(self, vendor, model, serial, coffee):
        super().__init__("Ксерокс", vendor, model, serial)
        self.coffee = coffee

    def __str__(self):
        return super().__str__() + f"\nУмеет варить кофе: {self.coffee}"

    @classmethod
    def create(cls):
        vendor, model, serial = super().create()
        coffee = input("Умеет варить кофе: ")
        return cls(vendor, model, serial, coffee)


stock = Stock("Подразделение программистов", "Отдел маркетинга", "Бухгалтерия", "Департамент уборки")
stock.equipments.append(Printer("Xerox", "DocuPrint P8E", "123-456", "Laser"))
stock.equipments.append(Scanner("Canon", "LIDE 210", "789-012", "2440"))

while True:
    print("Что делаем?\n")
    print("\t1. Приём техники на склад")
    print("\t2. Передача техники в департамент")
    print("\t3. Отобразить содержимое склада")
    print("\t4. Выйти")
    answer = get_answer(1, 2, 3, 4)
    if answer == 1:
        stock.add_equipment()
    elif answer == 2:
        stock.move_equipment()
    elif answer == 3:
        stock.show_equipments()
    else:
        break