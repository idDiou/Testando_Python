#comece com uma cópia do seu programa anterior
#escreva uma função chamada make_great()
#que modifique a lista de mágicos acrescentando a expressão O Grande ao nome de cada mágico
#chame show_magicians() para ver se a lista foi realmente modificada

magicians = ['Paterson', 'Piter', 'Roberto Carlos', 'Salsicha']
magos = []
def show_magicians(magicos):
    for magico in magicos:
        print('ola meu bom amigo', magico,'como vai essa vida de magia em?')

def make_great(magicos):
    while magicos:
        alterando = magicians.pop()
        alterando = alterando+' O Grande'
        magos.append(alterando)

make_great(magicians)

show_magicians(magos)
