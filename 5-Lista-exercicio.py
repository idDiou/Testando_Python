convidados = ['Jesus', 'Elias', 'Paulo']

#tirando informação da lista para poder colocar método
Jesus = convidados[0]
print('você foi convidado',Jesus.strip())
#podendo colocar o metodo strip  ^^^^^ na variavel, ajustando assim o espaço de linha

print('você foi convidado', convidados[1])
print('você foi convidado', convidados[2])
print('Elias: não poderei ir, estou aguardando junto do pai.')
ausente = convidados.pop(1)
print('Lista atual de confirmados:\n', Jesus,'\n', convidados[1])
print('não poderão comparecer:\n', ausente)

convidados.insert(2, 'Moisés')
convidados.insert(3, 'Dio')
convidados.append( 'Pedro')

print ('**um local maior para a celebração foi encontrado**')
print('Vocês foram convidados:\n', convidados[2],'\n', convidados[3],'\n', convidados[4])

print('**a mesa do local não chegará a tempo, apenas dois convidados**')
Paulo = convidados.pop(1)
print('sinto muito', Paulo, 'infelizmente não haverá lugar para todos')
Moises = convidados.pop(1)
print('sinto muito', Moises, 'infelizmente não haverá lugar para todos')
Pedro = convidados.pop(2)
print('sinto muito', Pedro, 'infelizmente não haverá lugar para todos')
print('ola', convidados[0],'eu sou o', convidados[1],'e te amo Jesus')

len(convidados)


