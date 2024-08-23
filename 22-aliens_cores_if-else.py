cores = ['azul', 'verde', 'vermelho', 'roxo', 'amarelo']
pontuaçao = 0
numero = 0


for cor in cores:
    if cor == 'verde':
        pontuaçao = +5
        print('você recebeu 5 pontos')
    elif cor == 'azul':
        pontuaçao = +10
        print('você recebeu 10 pontos')
    elif cor == 'amarelo':
        pontuaçao == +20
        print('você recebeu 20 pontos')
    else:
        print('alien esquivou')

print ('sua pontuação:', pontuaçao)
