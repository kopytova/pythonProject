list_worker = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in list_worker:
    name = i.split()[-1]
    name = name.lower()
    name = name.title()
    print(f'Привет, {name}!')
