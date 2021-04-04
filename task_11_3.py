class NotNumber(Exception):

    def __init__(self, txt):
        self.txt = txt


numbers = []


def cut_sign(maybe_num):
    if maybe_num.startswith('-'):
        return -1, maybe_num[1:]
    else:
        return 1, maybe_num


def cut_frac(maybe_num):
    if "." in maybe_num:
        i, f = maybe_num.split(".")
        if f.isdigit():
            return int(f) / 10 ** len(f), i
        else:
            raise NotNumber(f"Дробная часть {f} не является числом")
    else:
        return 0, maybe_num


while True:
    try:
        maybe_num = input("Введите следующее число: ")
        if maybe_num == "stop":
            break

        sign, maybe_num = cut_sign(maybe_num)
        frac, maybe_num = cut_frac(maybe_num)
        if not maybe_num.isdigit():
            raise NotNumber(f"{maybe_num} не является числом")
        numbers.append(sign * (int(maybe_num) + frac))
    except NotNumber as e:
        print(e)

print(numbers)
