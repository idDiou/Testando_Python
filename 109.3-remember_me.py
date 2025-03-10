#união dos dois códigos anteriores
#utilizar um bloco try pra tentar buscar o nome do usuário na memória
#utilizar except para caso não encontre
import json

username = input('ola, qual o seu nome?\n')

try:
    filename = username+'.json'
    with open (filename) as f_obj:
        username = json.load(f_obj)
    print('bem vindo de volta ' + username + '!')
except FileNotFoundError:
    filename = username+'.json'
    with open (filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print('Hey ' + username + ', Eu vou lembrar de você da próxima vez!')
