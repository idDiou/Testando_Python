usuarios = ['Leo', 'David', 'Dio', 'Otavio', 'admin']
especiais = ['admin']
for usuario in usuarios:
    if usuario in especiais:
        print('Boas Vindas Administrador')
    if usuario not in especiais:
        print('bem vindo', usuario)

#teste pra ver se tem gente na lista, python interpreta uma lista vazia como false
if usuarios:
    print('tem gente na lista')
else:
    print('precisamos adicionar membros na lista')