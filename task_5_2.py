n = int(input('Enter number: '))
odd_gen = (num for num in range(1, n+1, 2))
print(*odd_gen)

i = 0
n = 26
print([i for i in range(n) if i % 2 != 0])