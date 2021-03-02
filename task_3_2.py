num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
            'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(num_en):
    num_ru = None
    if num_en.lower() in num_dict:
        num_ru = num_dict[num_en.lower()]
        if num_en == num_en.title():
            num_ru = num_ru.title()

    return num_ru

num_ru = num_translate_adv(input('Enter a digit: '))
print(num_ru)