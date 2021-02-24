meteo_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
meteo_quoted_list = []

for i in meteo_list:
    s = ''
    if i[0] == '+' or i[0] == '-':
        s = i[0]
        j = i[1::]
        if j.isdigit():
            j = int(j)
            k = f'"{s}{j:02d}"'
            meteo_quoted_list.append(k)
        else:
            meteo_quoted_list.append(i)
    else:
        if i.isdigit():
            i = int(i)
            k = f'"{i:02d}"'
            meteo_quoted_list.append(k)
        else:
            meteo_quoted_list.append(i)

result = ' '.join(meteo_quoted_list)

print(result.capitalize())


