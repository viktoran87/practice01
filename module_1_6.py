my_dict={'Viktor': 1987, 'Anton': 1990, 'Alexey': 2001}
print(my_dict)
print(my_dict['Viktor'])
print(my_dict.get('Masha'))
my_dict.update({'Petya': 1984, 'Max': 2007})
print(my_dict.pop('Alexey'))
print(my_dict)
# множество
my_set={1, 2, 3, 4, 5, 4, 3, 2, 1,'Герань', 'Акация', 'Герань', (6, 7, 8, 9)}
print(my_set)
my_set.update((1, 2, 3, 4, 5), [6, 7, 8, 9])
my_set.discard('Акация')
print(my_set)