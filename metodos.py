Fruits = ['apples', 'pears', 'mangos', 'melon']

# get

print(Fruits[1])

# get length

print(len(Fruits))

# append

Fruits.append('grapes')
print(Fruits)

# insert

Fruits.insert(2,'strawberries')
print(Fruits)

# remove

Fruits.remove('strawberries')
print(Fruits)

# remove con pop (por posicion)

Fruits.pop(2)
print(Fruits)

# reverse

Fruits.reverse()
print(Fruits)

# cambio de valor en determinada posicion de la lista

Fruits[0] = 'cherries'
print(Fruits)
