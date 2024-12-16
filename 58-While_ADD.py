respostas = {}

ativo = True

while ativo:
    nome = input('\nQual o seu nome?\n')
    resposta = input('\nQual montanha você gostaria de escalar um dia?\n')
    respostas[nome] = resposta
    repeat = input('se quiser cadastrar outra pessoa digite "Y", Caso contrário digite qualquer coisa\n')
    if repeat == 'yes' or repeat == 'Yes' or repeat == 'Sim' or repeat == 'sim' or repeat == 's' or repeat == 'y' or repeat == 'si':
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPerfeito, vamos começar de novo')
    else:
        print('\nencerrando...')
        ativo = False
print('resultado das perguntas:\n')
for nome, resposta in respostas.items():
    print(nome, 'gostaria de subir', resposta + '.')