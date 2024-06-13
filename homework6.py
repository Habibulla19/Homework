my_dict = {'Habib': 1997, 'Denis': 1995, 'Anton': 1990}
print(my_dict)
print(my_dict['Habib'])
print(my_dict.get('Andrey','Нет такого ключа'))
my_dict['Vlodimir'] = 1991
my_dict['Svetlana'] = 1987
print(my_dict)
my_dict.pop('Habib')
print(my_dict)

#my_dict = {'Habib': 1997, 'Denis': 1995, 'Anton': 1990}
#update({'Kirill': 1976, 'Artem': 1993})
#print(my_dict)
#my_dict.pop('Habib')
#print(my_dict)
#a = my_dict.pop('Denis')
#print(a)
#my_dict = {'Habib': 1997, 'Denis': 1995, 'Anton': 1990}
#print(my_dict.keys())
#print(my_dict.values())
#print(my_dict.items())

my_set = {1, 3, 7, 9, 11, 7, 13, 9, 3, 11, 'String', True, 9.5}
print(my_set)
my_set.update({'Habib', False})
print(my_set)
my_set.discard(9)
print(my_set)

