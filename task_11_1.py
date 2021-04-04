class Date:

    def __init__(self, date):
        self.day, self.month, self.year = Date.validate(*date.split("-"))

    @staticmethod
    def validate(d, m, y):
        if not d.isdigit(): raise ValueError("День должен быть числом")
        if not m.isdigit(): raise ValueError("Месяц должен быть числом")
        if not y.isdigit(): raise ValueError("Год должен быть числом")

        day, month, year = int(d), int(m), int(y)
        if year < 1: raise ValueError("Год должен быть больше 1")
        if not 1 <= month <= 12: raise ValueError("Месяц должен быть от 1 до 12")

        max_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if not 1 <= day <= max_day[month]: raise ValueError(f"День должен быть от 1 до {max_day[month]}")

        if month == 2 and day == 29:
            if year % 4 or (year % 100 == 0 and year % 400):
                raise ValueError(f"Год {year} не високосный")

        return day, month, year


date = Date("29-02-2020")
print(f"{date.day:02}.{date.month:02}.{date.year:04}")
