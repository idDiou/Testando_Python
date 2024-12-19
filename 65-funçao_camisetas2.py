#modifique a função camisetas de modo que as camisetas sejam grandes por default
#com uma mensagem eu amo python
#crie uma camiseta grande e outra média com a mensagem default
#e uma camiseta de qualquer tamanho com uma mensagem diferente

def camisetas(tamanho='grande', estampa='Eu amo python'):
    print('uma camiseta de tamanho', tamanho,'e escrito "'+estampa+'"')

camisetas()
camisetas('média')

camisetas('pequena', 'Eu ando de skate')