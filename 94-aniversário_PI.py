with open ('pi_million.txt') as conteudo_arquivo:
    pi  = conteudo_arquivo.readlines()

pi_string = ''
for numero in pi:
    pi_string += numero
    print(pi_string)

print('testamos um milhão de digitos PI, agora vamos testar se o seu aniversário está contido ai no meio')
while True:
    aniversario = input('escreva sua data de nascimento no seguinte formato, ddmmaa\n')
    if aniversario == 'cancel':
        break
    if aniversario in pi_string:
        print('seu aniversário está contido em pi')
    else:
        print('seu aniversário não está contido em pi')