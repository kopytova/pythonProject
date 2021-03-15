from sys import argv
from itertools import islice

with open('bakery.csv', 'r', encoding='utf-8') as data_output:
    el_bakery_gen = (el for el in data_output)
    elems = []
    if len(argv) == 1:
        elems = list(el_bakery_gen)
    elif len(argv) == 2:
        elems = islice(el_bakery_gen, int(argv[1]) - 1, None)
    else:
        elems = islice(el_bakery_gen, int(argv[1]) - 1, int(argv[2]))

    print(*elems)
