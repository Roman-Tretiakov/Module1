#2:
immutable_var = (0.0, [2, 3, 4], True, 'tuple')

print(immutable_var)

#3:
#call error: 'tuple' object does not support item assignment
#immutable_var[1] = [5, 6]

#not error:
immutable_var[1][1] = 33

print(immutable_var)

#4:
mutable_list = ['apple', 1, True, 5.5]

print(mutable_list)

mutable_list[0] = 'bananas'
mutable_list[1] = '1'
mutable_list[2] = False
mutable_list[3] = [0, 1, 2]
mutable_list.append(100)
mutable_list.extend(['pear', 'cherry'])

print(mutable_list)

