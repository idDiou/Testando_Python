#função para o exercício 79, importando funções de outros módulos
def make_pizzas(*ingredientes):
    print('--fazendo uma pizza com os seguintes ingredientes--')
    for ingrediente in ingredientes:
        print('*'+ingrediente +'*')