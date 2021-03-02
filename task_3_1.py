num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
            'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(num_en):
    if num_en in num_dict:
        return num_dict[num_en]
    else:
        return None


num_ru = num_translate(input('Enter a digit: '))
print(num_ru)
