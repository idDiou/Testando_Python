def pessoa(nome, sobrenome, idade=''):
    person = {'primeiro': nome, 'segundo': sobrenome}
    if idade:
        person['idade'] = idade
    return person

musico = pessoa('Jimi', 'hendrix')
print(musico)

lutador = pessoa('myke', 'Tyson', 21)
print(lutador)