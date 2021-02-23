
seconds = int(input('Введите временной интервал в секундах: '))

ss = (seconds % 60)
minutes = seconds // 60
mm = (minutes % 60)
hh = (minutes // 60)

print("%02d:%02d:%02d" % (hh, mm, ss))
