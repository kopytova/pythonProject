import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Егор', 'Виталий'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for (i, j) in itertools.zip_longest((tutors), (classes)):
    tup = (i, j)
    print(tup)



import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Егор', 'Виталий'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for (i, j) in itertools.zip_longest((tutors), (classes)):
    print((i, j))

