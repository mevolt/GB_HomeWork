# Маланчев Павел Андреевич
# Домашнее задание 1

# Задание 1.

duration = int(input("Введите количесвто секунд: "))

seconds = duration % 60
minutes = int(duration / 60) % 60
hours = int(duration / 60 / 60) % 60
days = int(duration / 60 / 60 // 24)

print(days, 'дня', hours, 'часа', minutes, 'минут', seconds, 'секунд')


# Задание 2.

sum1 = 0
sum2 = 0
num_list = list()
for number in range(1, 1001, 2):
    num_list.append(number ** 3)

for index in range(len(num_list)):
    num_sum = 0
    i = num_list[index]
    while i:
        num_sum += i % 10
        i = i // 10
    if num_sum % 7 == 0:
        sum1 += num_list[index]
    num_list[index] += 17
    num_sum = 0
    i = num_list[index]
    while i:
        num_sum += i % 10
        i = i // 10
    if num_sum % 7 == 0:
        sum2 += num_list[index]
print(sum1)
print(sum2)


# Задание 3.

for i in range(100):
    number_str = str(i + 1)
    number_list = list(number_str)
    if int(number_list[-1]) == 1 and i + 1 != 11:
        print('{} процент'.format(i + 1))
    elif int(number_list[-1]) > 1 and int(number_list[-1]) <= 4:
        if i + 1 > 10 and i + 1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))

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

print(num_translate('four'))




#nums = ['1578.4', '892.4', '354.1', '871.5']
#print(sum(map(float, nums)))
