s = '''Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели.'''
print(s)
s = s.lower()
counter = 0

for i in s.split():
    # if i[0] == 'е':
    if i.find('е', 0, 1) != -1:
        counter += 1

print()
print('Количество слов:', counter)



