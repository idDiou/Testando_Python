#escreva um programa que pergunte qual o numero favorito do usuário
#use Json.Dump() para armazenar esse numero em um arquivo
#escreva um programa separado que leia esse valor e apresente a mensagem
#"eu sei qual é o seu numero favorito é............"

import json
info_user = {}

while True:
    username = input('ola, qual o seu nome?\n')
    filename = username.lower()+'.json'
    try:
        with open(filename) as file:
            info_user = json.load(file)
            print('bem vindo de volta ' +info_user['nome']+' seu numero favorito é o ' + info_user['num_fav'])

    except:
        info_user['nome'] = username
        info_user['num_fav'] = str(input('hey ' + username +' vejo que é sua primeira vez por aqui ' + 'qual o seu numero favorito?\n'))
        with open(filename, 'w') as file:
            json.dump(info_user, file)
