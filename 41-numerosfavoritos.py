#Crie um Dicionário chamado Lugares_Favoritos
#pense em três nomes para usar como chaves do dicionário
#e armazene de um a três lugares favoritos para cada pessoa.
#percorra o dicionário com um laço e apresente o nome de cada pessoa e de seus lugares favoritos.

Lugares_Fav = {'Katoryn':{'*Floresta', '*Praça', '*Cama',}, 'Dio': {'*Em Frente ao computador', '*Com Deus', '*Com Katoryn'}, 'Antonio': {'*Skibidi', '*dopdop', '*YesyES'}}
Feminino = ['Katoryn']

for nome, info in Lugares_Fav.items():
    print('os lugares favorito de', nome+':')
    for lugares in info:
        print(lugares)