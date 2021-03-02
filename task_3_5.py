from random import choice

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

used_nouns = []
used_adverbs = []
used_adjectives = []


def build_jokes(n, can_repeat=True):
    if (not can_repeat and (n > len(nouns) or n > len(adverbs) or n > len(adjectives))):
        return "ERROR: n is too much"
    jokes = []
    for i in range(0, n):
        while (True):
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)
            if can_repeat or not (noun in used_nouns or adverb in used_adverbs or adjective in used_adjectives):
                used_nouns.append(noun)
                used_adverbs.append(adverb)
                used_adjectives.append(adjective)
                jokes.append(f'{noun} {adverb} {adjective}')
                break
    return jokes


print(build_jokes(5, False))
