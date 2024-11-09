#crie dois dicionários que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people
#Percorra sua lista de pesssoas com um laço. à medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa

people = {'Rogerio':{'profissão': 'advocacia', 'moradia': 'gravatai', 'nome': 'Rogerio cabral borges junior'},
          'Simone':{'profissão': 'política', 'moradia': 'cachoeirinha', 'nome': 'Simone Silva de Almeida'},
          'Claudia':{'profissão': 'Construção', 'moradia': 'bosque encantado', 'nome': 'Claudia Bruce Resmin'}}
feminino = ['Claudia', 'Simone']

for user, info in people.items():
    if user in feminino:
        print('a ' + user, 'é muie e mora em ' + info['moradia'] + ', e trabalha com', info['profissão'])
    if user not in feminino:
        print('o ' + user, 'é omi e mora em ' + info['moradia'] + ', e trabalha com', info['profissão'])

#feito