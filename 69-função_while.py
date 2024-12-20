def formando_nomes(first_name, last_name):
    full_name = first_name+ ' ' + last_name
    return full_name.title()

while True:
    print('digite "q" a qualquer momento para sair do programa')
    print('\npor favor me diga o seu nome:\n')
    f_name = input('first name: ')
    if f_name == 'q':
        break
    l_name = input('last name:')
    if l_name == 'q':
        break
    nome_formado = formando_nomes(f_name, l_name)
    print('\nOla, '+nome_formado+'!')