#  Home_work

region = {
    'John': {
        'N': 3056,
        'S': 8463,
        'E': 8441,
        'W': 2694
    },
    'Tom': {
        'N': 4832,
        'S': 6786,
        'E': 4737,
        'W': 3612
    },
    'Anne': {
        'N': 5239,
        'S': 4802,
        'E': 5220,
        'W': 1859
    },
    'Fiona': {
        'N': 3056,
        'S': 3645,
        'E': 8821,
        'W': 2451
    }
}

for x in region:
    print(x)
    for y in region[x]:
        print(y, ':', region[x][y])

name = input('Имя: ')
r = input('Регион: ')
print(region[name][r])
new = int(input('Новое значение: '))
region[name][r] = new
print(region[name])
