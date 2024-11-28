#Ingressos para o Cinema
#um cinema cobra preços diferentes de acordo com a idade de uma pessoa.
#se uma pessoa tiver menos de 3 anos de idade, o ingresso será gratuito.
#se tiver entre 3 e 12 anos, o ingresso custará 10 dolares.
#se tiver mais de 12 anos o ingresso custará 15 dólares.
#escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso

atendendo = True
idade = 0

#tomar cuidado com a entrada de informação pelo input, prestar atenção em transformar dados str em int

while atendendo:
    idade = input('\nOlá, quantos anos você tem?\n')
    idade = int(idade)
    if idade <= 3:
        print('para pessoas menores de 3 anos o ingresso é gratuito')
    if idade > 3 and idade <= 12:
        print('para você o ingresso sai a 10 dolares')
    if idade > 12:
        print('para pessoas com mais de 12 anos o ingresso custa 15 dólares.')