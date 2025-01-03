#crie uma lista de nomes de mágicos.
#passe a lista para uma função chamada "show_magicians()"
#que exiba o nome de cada mágico da lista

magicians = ['Paterson', 'Piter', 'Roberto Carlos', 'Salsicha']

def show_magicians(magicos):
    for magico in magicos:
        print('ola meu bom amigo', magico,'como vai essa vida de magia em?')

show_magicians(magicians)