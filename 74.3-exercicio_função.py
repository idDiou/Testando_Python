#comece com uma cópia do seu programa anterior
#chame a função "make_great()" com uma cópia da lista Magicians
#chame cada lista para mostrar que ambas estão inalteradas

def show_magicians(magicos):
    for magico in magicos:
        print('ola meu bom amigo', magico,'como vai essa vida de magia em?')

def make_great(magicos, magao):
    while magicos:
        alterando = magicos.pop()+' O Grande'
        for mag in magicos:
            print('tornando o '+ mag +' em grande')
            print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        magao.append(alterando)

magicians = ['Paterson', 'Piter', 'Roberto Carlos', 'Salsicha']
magos = []

make_great(magicians[:], magos)
show_magicians(magos)

print(magicians)
print(magos)