n = input('Введите целое положительное число: ')
length = len(n)
i = 0
max = n[0]
while i < length:
    if n[i] > max:
        max = n[i]
    i += 1
print(max)