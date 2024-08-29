#versão 1:
#lista = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
#numlist = 4

#print('seu lugar de chegada é:', lista[numlist])
#print('as demais colocações:')
#for colocaçao in lista:
#    print(colocaçao)

#versão 2:

lista = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
var = 0
for loop in lista:
    if var == 0:
        print('parabéns você chegou em: 1', loop)
        var = 1
    elif var == 1:
        print('parabéns você chegou em: 2', loop)
        var = 2
    elif var == 2:
        print('parabéns você chegou em: 3', loop)
        var = 3
    elif var == 3:
        print('parabéns você chegou em: 4', loop)
        var = 4
    elif var == 4:
        print('parabéns você chegou em: 5', loop)
        var = +5
    elif var == 5:
        print('parabéns você chegou em: 6', loop)
        var = 6
    elif var == 6:
        print('parabéns você chegou em: 7', loop)
        var = 7
    elif var == 7:
        print('parabéns você chegou em: 8', loop)
        var = 8
    elif var == 8:
        print('parabéns você chegou em: 9', loop)
        var = 9