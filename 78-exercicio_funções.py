#SANDUICHES
#escreva uma função que aceite uma liste de itens que uma pessoa quer em um sanduiche
#a função deve ter um parametro que agrupe tantos itens quanto forem fornecidos pela chamada da função
#e deve apresentar um resumo do sanduiche pedido
#chame a função três vezes usando um numero diferente de argumentos de cada vez

def sanduiches(tamanho, *ingredientes):
    print('Saindo um sanduiche ' + tamanho + ', com os seguintes ingredientes:')
    for ingrediente in ingredientes:
        print('-' + ingrediente)

sanduiches('grande', 'catupiry', 'tomate', 'mortadela')
sanduiches('pequeno', 'amendoim', 'maionese', 'queijo', 'carne')
sanduiches('médio', 'Brocolis', 'beterraba', 'Proteina de Soja', 'alface')