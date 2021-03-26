class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, side):
        print(f'Машина {self.name} повернула {"налево" if side == 0 else "направо"}')

    def show_speed(self):
        return (f'Автомобиль едет со скоростью {self.speed} км/час')


class TownCar(Car):
    def show_speed(self):
        return (f'Автомобиль {self.name} едет с превышением скорости. Скорость автомобиля: {self.speed}' \
                    if self.speed > 60 else f'{self.name} едет со скоростью {self.speed} км/час')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return (
            f' Очень быстрый спортивный автомобиль {self.name} едет с превышением скорости. Он спортивный, ему можно!'
            if self.speed > 60 else f'{self.name} едет со скоростью {self.speed} км/час')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('Nissan micro', 'синий', 50)
town_car.go()
town_car.turn(0)
print(town_car.show_speed())
town_car.turn(1)
town_car.stop()
print()

sport_car = SportCar('Porsche 911', 'красный', 140)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.stop()
print()

work_car = WorkCar('Газель Next', 'белый', 60)
work_car.go()
work_car.turn(1)
work_car.turn(0)
print(work_car.show_speed())
work_car.stop()
print()

police_car = PoliceCar('Ford focus', 'синий', 70)
police_car.go()
police_car.turn(0)
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
