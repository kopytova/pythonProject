class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def mass_calculation(self, density=25, thickness=5):
        mass = int(self._length * self._width * density * thickness / 1000)
        return mass

road_square = Road(5000, 20)
print(f'{road_square.mass_calculation()} тонн асфальта')