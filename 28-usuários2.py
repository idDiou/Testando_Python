Cadastrados = ['Leo', 'David', 'Dio', 'Otavio', 'admin']
Novos = ['Leo', 'admin', 'Malagueta', 'dio']

for cadastro in Novos:
    if cadastro.lower() in Cadastrados:
        print ('o nome de usuário:', cadastro, 'Já está em uso')
    elif cadastro.upper() in Cadastrados:
        print ('o nome de usuário:', cadastro, 'Já está em uso')
    elif cadastro.title() in Cadastrados:
        print ('o nome de usuário:', cadastro, 'Já está em uso')
    else:
        print('o nome de usuário:', cadastro, 'foi cadastrado com sucesso')