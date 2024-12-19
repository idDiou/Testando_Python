#com nome do meio agora

def formando_nome(nome, sobrenome, meio=''):
    if meio:
        nome_completo = nome + ' ' + meio + ' ' + sobrenome
    else:
        nome_completo = nome + ' ' + sobrenome
    return nome_completo.title()

musico = formando_nome('jimi', 'hendrix')
print(musico)

grandelfo = formando_nome('Gandalf', 'Nori', 'Papoula')
print(grandelfo)