#2:
my_dict = {'Ivan': 2000, 'Petr': 1970, 'Mariya': 1991, 'Elizaveta': 2015}
existing_name = 'Elizaveta'
not_existing_name = 'Semen'
existing_value = my_dict[existing_name]
not_existing_value = my_dict.get(not_existing_name)

print(f'Dictionary: {my_dict}')

my_dict.update({'Elena': 1980, 'Katya': 2017})
value = my_dict.pop(existing_name)

print(f'Existing value: {existing_value}')
print(f'Not existing value: {not_existing_value}')
print(f'Deleted value: {value}')
print(f'Modified dictionary: {my_dict}')

#3:
my_set = {(1, 2, 3), 10, True, 'Set', 99.99, 10, 'Set', 99.99, (1, 2, 3)}

print(f'Set: {my_set}')

my_set.update([100, 'Apple'])
my_set.discard(True)

print(f'Modified set: {my_set}')
