def val_checker(is_valid):
    def _val_checker(func):
        def wrapper(x):
            if is_valid(x):
                return func(x)
            else:
                raise ValueError(f'{x} is negative')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
b = calc_cube(0)
print(a)
print(b)