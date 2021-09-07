# Задание 1.

def num_translate(eng):
    my_dictionary = {'one': 'один',
                     'two': 'два',
                     'three': 'три',
                     'four': 'четыре',
                     'five': 'пять',
                     'six': 'шесть',
                     'seven': 'семь',
                     'eight': 'восемь',
                     'nine': 'девять',
                     'ten': 'десять'}
    return my_dictionary.get(eng)


print(num_translate(input('Введите число на английском: ')))


# Задание 2.


def num_translate_adv(eng):
    my_dictionary2 = {'one': 'один',
                     'two': 'два',
                     'three': 'три',
                     'four': 'четыре',
                     'five': 'пять',
                     'six': 'шесть',
                     'seven': 'семь',
                     'eight': 'восемь',
                     'nine': 'девять',
                     'ten': 'десять'}
    if eng.istitle() and my_dictionary2.get(eng.lower()):
        return my_dictionary2.get(eng.lower()).title()
    else:
        return my_dictionary2.get(eng)


print(num_translate_adv(input('Введите число на английском: ')))


# Задание 3.


def thesaurus(*args):
    my_dictionary3 = dict()
    for name in args:
        i = name[0]
        if i not in my_dictionary3:
            my_dictionary3[i] = []
        my_dictionary3[i].append(name)
    return my_dictionary3


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# Задание 5.


NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat_words=False):
    jokes = []
    if not repeat_words:
        nouns_copy = NOUNS.copy()
        random.shuffle(nouns_copy)
        adverbs_copy = ADVERBS.copy()
        random.shuffle(adverbs_copy)
        adjectives_copy = ADJECTIVES.copy()
        random.shuffle(adjectives_copy)
        for num, (noun, adverb, adjective) in enumerate(zip(nouns_copy, adverbs_copy, adjectives_copy)):
            jokes.append(f'{noun} {adjective} {adverb}')
            if num == n:
                break
    else:
        for _ in range(n):
            jokes.append(f'{random.choice(NOUNS)} {random.choice(ADVERBS)} {random.choice(ADJECTIVES)}')
    return jokes



