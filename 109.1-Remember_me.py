#agora vamos escrever um programa que faça uma saudação a um usuário cujo nome já esteja armazenado
import json

filename = 'dsadasdio.json'

with open (filename) as f_obj:
    username = json.load(f_obj)
    print('bem vindo de volta ' + username + '!')

