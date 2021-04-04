class Complex:

    def __init__(self, d, i):
        self.d, self.i = d, i

    def __str__(self):
        if self.d == 0 and self.i == 0:
            return "0"
        elif self.d == 0:
            return f"{self.i}i"
        elif self.i == 0:
            return f"{self.d}"
        else:
            sign = "+" if self.i > 0 else "-"
            return f"{self.d}{sign}{abs(self.i)}i"

    def __add__(self, other):
        return Complex(self.d + other.d, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.d * other.d - self.i * other.i, self.d * other.i + self.i * other.d)


c1 = Complex(2, -1)
c2 = Complex(4, 5)
print(c1 + c2)
print(c1 * c2)
