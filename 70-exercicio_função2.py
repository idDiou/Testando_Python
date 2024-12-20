#escreva uma função chamada make_album()
#que construa um dicionário descrevendo um album musical
#a função deve aceitar o nome de um artista e o titulo de um album
#e deve devolver um dicionário contendo essas duas informações.
#use a função para cirar três dicionários que representem duas informações
#apresente cada valor devolvido para mostrar o que os dicionários estão armazenando as informações corretamente

#acrescente um parametro opcional em make_album() que permita armazenar o numero de faixas em um album.
#se a linha que fizer a chamda incluir um valor para o numero de faixas, acrescente esse valor ao dicionário do album.
#faça pelo menos uma nova chamada da função incluindo o numero de faixas em um album.

#insira um laço while que permita a entrada de usuários
coleção = {}

def make_album(artista, album, qtd_musica = 0):
    coleção[artista] = {'albuum':album, 'musicass': qtd_musica}

while True:
    print('digite "q" para finalizar o programa')
    print('\ndigite um artista e um album para armazenarmos')
    
    artist = input('artista: ')
    if artist == 'q':
        break
    alboum = input('album: ')
    if alboum == 'q':
        break
    music = str(input('quantidade de musicas: '))

    make_album(artist, alboum, qtd_musica= music)

print (coleção)

for artistas, info in coleção.items():
    musicas = info['musicass']
    albuns = info['albuum']
    print(artistas,'tem o seguinte album:', albuns, '\ncom:', musicas, 'musicas')