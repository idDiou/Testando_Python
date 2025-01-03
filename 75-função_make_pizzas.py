#o asterico diz a python para criar uma tupla vazia chamada toppings e reunir os valores recebidos nessa tupla
def make_pizzas(*toppings):
    print('--fazendo uma pizza com os seguintes ingredientes--')
    for ingredientes in toppings:
        print('*'+ingredientes +'*')
make_pizzas('pepperoni')
make_pizzas('mushrooms', 'pimentão', 'queijo extra')