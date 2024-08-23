my_dict = {'Moscow': 12506458, 'St. Petersburg': 5384342, 'Kazan': 1257391, 'Novosibirsk': 1625631}
print('Dist: ', my_dict)
print('Existing value: ', my_dict.get('Kazan'))
print('Not existing value: ', my_dict.get('Samara', 'Такого города нет'))
my_dict.update ({'Penza': 523553, 'Perm': 1051583}) # Добавление в словарь
s = my_dict.pop('St. Petersburg')
print('Deleted value: ', s)
print('Modified dictionary: ', my_dict)
print()

my_set = {120, 130, (1, 2, 3),'OOO', (1, 2,3), 130, 120, 7, 'OOO', 2, 5}
print('Set :', my_set)
my_set.update({'13', 16}) # Добавляем во множество строчный элемент и число
my_set.discard((1, 2, 3))
print('Modified set: ', my_set)