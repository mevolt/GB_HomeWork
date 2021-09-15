tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А',]


def my_gen(item1, item2):
    i = len(item1) - len(item2)
    if i > 0:
        for _ in range(i):
            item2.append(None)
    for tutor, klass in zip(item1, item2):
        yield (tutor, klass)


my_genera = my_gen(tutors, klasses)
print(next(my_genera))
print(next(my_genera))
print(next(my_genera))
print(next(my_genera))
print(next(my_genera))
print(next(my_genera))
print(next(my_genera))


