#escreva um laço que peça ao usuario para fornecer uma série de ingredientes para uma pizza, até que o valor 'quit' seja
#fornecido. À medida que cada ingrediente é especificado, apresente uma mensagem informando que você acrescentará esse
#ingrediente à Pizza
Tamanho = ''

Tamanho = input('\npor favor escolha o tamanho de sua pizza\n')
ingrediente = ''
ingredientes = []
vezes = 0

flag = True

print('vamos escolher os ingredientes, caso deseje finalizar, apenas digite "finalizar"')

while flag:  
    vezes += 1
    if vezes == 1:
        ingrediente += input('quais você vai querer?\n')
        ingredientes.append(ingrediente)
        for pizza in ingredientes:
            print('perfeito sua pizza tem atualmente:\n'+ pizza)
    elif vezes >= 2:
        ingrediente = ''
        ingrediente += input('algo mais?\n')
        ingredientes.append(ingrediente)
        print('perfeito sua pizza tem atualmente:')
        for pizza in ingredientes:
            print(pizza)
    for ingrediente in ingredientes:
        if ingrediente == 'finalizar':
            flag = False

borda = input('muito bem, agora falta apenas a borda, você vai querer ela de que?\n')

print('muito bem, então nós temos uma pizza', Tamanho +', com borda de ' + borda, 'com os seguintes ingredientes:')
for pizza in ingredientes:
    if pizza != 'finalizar':
        print(pizza)
