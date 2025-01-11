#o asterico diz a python para criar uma tupla vazia chamada toppings e reunir os valores recebidos nessa tupla

def make_pizzas(*ingredientes):
    print('--fazendo uma pizza com os seguintes ingredientes--')
    for ingrediente in ingredientes:
        print('*'+ingrediente +'*')
