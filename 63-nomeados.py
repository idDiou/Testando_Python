def desc_pet(tipo, nome):
    print('eu tenho um '+tipo)
    print('o nome do meu', tipo, 'é', nome)

#a função não mudou, entretanto quando chamamos a função, dizemos explicitamente a python a qual parametro cada 
#argumento deve corresponder.
desc_pet(nome='Alex', tipo='leão')
