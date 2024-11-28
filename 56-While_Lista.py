usuarios_N = ['Dio', 'Rogerio', 'Daaparty', 'Antonio', 'Miguel']
Usuarios_S = []


#mexendo com listas e While, utilizando o método pop para retirar de uma lista e o append para colocar em outra

#laço executa enquanto houver itens na lista usuarios_N

while usuarios_N:
    usuario_A = usuarios_N.pop()
    print('usuários verificados:', usuario_A.title())
    Usuarios_S.append(usuario_A)

print ('\nUsuários Confirmados:')
for usuario_S in Usuarios_S:
    print(usuario_S)