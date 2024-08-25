disponiveis= ['cogumelos', 'pimenta verde', 'pepperoni', 'queijo', 'abacaxi']
requisitados = ['cogumelos', 'batata frita', 'queijo']

#comparando listas

for requisitado in requisitados:
    if requisitado in disponiveis:
        print('adicionando',requisitado,'.')
    else:
        print('desculpe, não temos ', requisitado)