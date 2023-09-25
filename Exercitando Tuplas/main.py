tupla_1 = ('Valor_1', 2, 3.1, 'Kenzie Academy',
           ['Elemento1', 'Elemento2'], 'Kenzie Academy')
print(tupla_1)

print(tupla_1[-1])

print(len(tupla_1))

print(tupla_1.count('Kenzie Academy'))

print(tupla_1.index(3.1))

minha_lista = list(tupla_1)

minha_lista[-1] = 'Ultimo Elemento'

tupla_1 = tuple(minha_lista)

print(tupla_1)
