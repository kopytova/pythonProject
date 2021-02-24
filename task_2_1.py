composition = 15 * 3
print(isinstance(composition, int))

quotient = 15 / 3
print(isinstance(quotient, float))

quot = 15 // 2
print(isinstance(quot, int))

squared = 15 ** 2
print(isinstance(squared, int))



composition = 15 * 3
quotient = 15 / 3
quot = 15 // 2
squared = 15 ** 2

print(isinstance(composition, int), isinstance(quotient, float), isinstance(quot, int), isinstance(squared, int))


expression = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for i in expression:
    print(type(i))