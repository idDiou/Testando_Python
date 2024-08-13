players = ['jose', 'roberto', 'thiago', 'mamao']

#da mesma forma que range, a contagem para 1 numero abaixo
#exemplo: começa em 0 e termina em 2
#0, 1, 2 --pegando 3 elementos da lista
print(players[0:3])

#se omitir a primeira fatia, python inicia do começo
#nada na esquerda do indice
print (players[:3])

#também funciona pro final
print (players[1:])

print(players[:-2])