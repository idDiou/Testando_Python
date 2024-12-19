#utilizamos valores padrões nos parametros da função
#para que caso o valor não seja especificado ele tenha um valor por padrão.

def desc_pet(nome, tipo='cachorro'):
    print('eu tenho um '+tipo)
    print('o nome do meu', tipo, 'é', nome)

desc_pet(nome='Alex', tipo='leão')


#nesse caso, o tipo não é especificado, portanto puxa automáticamente o "cachorro"
desc_pet('amendoim')
