#tuplas são listas imutaveis, a diferença esta na sintexe, pois utiliza () ao invés de []
buffet = ('carne', 'arroz', 'feijão', 'alface', 'batata frita')

print('o que temos pro buffet hoje: ')
for comida in buffet:
    print(comida)


buffet = ('salsicha', 'hortelã', 'amendoim')

print('o que teremos no buffet amanhã:')
for comida in buffet:
    print(comida)