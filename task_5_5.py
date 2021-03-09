src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
dub = []

for i in src:
    if i in result:
        result.remove(i)
        dub.append(i)
    else:
        result.append(i)

print(result)
