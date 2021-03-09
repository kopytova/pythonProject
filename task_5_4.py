src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
def adjacent_pairs(num):
    sequence_object = iter(num)
    prev = next(sequence_object)
    for item in sequence_object:
        yield (prev, item)
        prev = item

pairs = adjacent_pairs(src)

for i in pairs:
    if i[1] > i[0]:
        result.append(i[1])

print(result)






