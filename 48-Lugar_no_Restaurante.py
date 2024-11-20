#escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar.
#se a resposta for maior que oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa.
#caso contrário, informe que sua mesa está pronta

pergunta = input('Vocês estão em quantos?\n')
pergunta = int(pergunta)

if pergunta >= 8:
    print('Vocês precisarão esperar até que uma mesa esteja liberada.')
elif pergunta <=8:
    print('há uma mesa disponível, me acompanhem por favor.')