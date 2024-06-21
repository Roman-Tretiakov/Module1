example = 'Топинамбур'

#2 first symbol:
print(example[0])

#3 last symbol:
print(example[-1])

#4 second half of the string:
index = len(example)//2

if index % 2 == 0:
    index -= 1

print(example[-index:])

#5 word is backwards:
print(example[::-1])

#6 each second symbol:
print(example[1::2])
