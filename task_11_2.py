class ZeroDevision(Exception):

    def __init__(self, txt):
        self.txt = txt



a = float(input("Делимое: "))
b = float(input("Делитель: "))

try:
    if b == 0: raise ZeroDevision("Делить на 0 нельзя!")
    print(round(a / b, 2))

except ZeroDevision as e:
    print(e)