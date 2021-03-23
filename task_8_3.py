def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: ' + str(type(arg)))
        return func(*args)
    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
print(a)
