def odd_generator(n):
    for num in range(1, n+1, 2):
        yield num

odd_numbers = odd_generator(11)
print(next(odd_numbers), next(odd_numbers), next(odd_numbers), next(odd_numbers), next(odd_numbers), next(odd_numbers))