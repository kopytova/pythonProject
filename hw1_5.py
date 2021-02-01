proceeds = int(input('Укажите выручку компании: '))
costs = int(input('Укажите издержки компании: '))
profit = int(proceeds) - int(costs)

if proceeds > costs:
    print(f'Компания работает с прибылью. Рентабельность составляет: {profit / proceeds * 100:.1f}%')
    staff = int(input('Укажите количество сотрудников в компании: '))
    print(f'Прибыль на одного сотрудника составила: {profit / staff:.1f}')
elif proceeds == costs:
    print('Компания работает "в ноль"')
else:
    print('Компания работает в убыток')