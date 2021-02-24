price_list = [60.30, 20.45, 70, 90.03, 55, 72.40, 42.13, 87, 88.70, 62, 20.07, 59.90, 98.2, 18.53, 58]
new_price_list = []
r = 'руб.'
k = 'коп.'
high = 'Пять самых высоких цен в списке: '

for price in price_list:
    rub = int(price)
    kop = int((price - rub) * 100)
    new_price_list.append(f'{rub} {r} {kop:02} {k}')

print(','.join(new_price_list))

print(id(new_price_list))

new_price_list.sort()

print(','.join(new_price_list))

print(id(new_price_list))

change_price_list = new_price_list.copy()

change_price_list.sort(reverse=True)

print(','.join(change_price_list))

print(high + ','.join(change_price_list[:5]))
