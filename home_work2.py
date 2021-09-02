# Задание 1.

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# Задание 2.

main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for item in main_list:
    quotes1 = ''
    quotes2 = ''
    quotes3 = ''
    for i in item:
        if i in '1234567890':
            quotes1 += i
        else:
            if quotes1:
                quotes3 += i
            else:
                quotes2 += i
    if not quotes1:
        main_list.append(item)
        continue
    quotes1 = f'{quotes2}{int(quotes1):02d}{quotes3}'
    main_list.append('"')
    main_list.append(quotes1)
    main_list.append('"')
print(main_list)

# Задание 4.

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in name_list:
    name = i.split()[-1].title()
    print('Привет,', name)

# Задание 5.

price_list = [23.34, 45.56, 23.3, 77.1, 34.5, 45.94, 30.33, 12.90, 75.12]
new_list = []
for price in price_list:
    roubles = int(price)
    cent = round((price - roubles) * 100)
    new_list.append(f'{roubles} руб {cent:02d} коп')
print(', '.join(sorted(new_list)))
print(', '.join(reversed(sorted(new_list))))


