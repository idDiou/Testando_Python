#fazendo com que o programa lembre nossa entrada
import json
username = input('qual o seu nome?\n')
filename = username+'.json'

with open (filename, 'w') as f_obj:
    json.dump(username, f_obj)

print('Hey ' + username + ', Eu vou lembrar de você da próxima vez!')