#Perfil do Usuário

#comece com uma cópia de um exercicio anterior o "user_profile"
#crie um perfil chamado build_profile() usando seu primeiro nome e o sobrenome, além de três outros pares valor que o descrevam

def perfil(first_name, last_name, **caracteristicas):
    Me = {}
    Me['first_name'] = first_name
    Me['last_name'] = last_name
    print('meu nome é', first_name, last_name,'essas são minhas características:')
    for key,value in caracteristicas.items():
        Me [key] = value
        print('\n*'+key +':\n')
        for chave in value:
            print('-'+chave)




perfil('dio', 'apenas', alimentos = ['alaminuta', 'hamburguer', 'batata frita'], Esportes = ['Ciclismo', 'Muay Thai'])
perfil('katoryn', 'foficute', alimentos = ['Doces', 'hamburguer', 'pizzas'], Esportes = ['caminhada', 'carDIO', 'ciclismo'])