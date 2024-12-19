def formando_nome(nome, sobrenome):
    nome_completo = nome + ' ' + sobrenome
    return nome_completo.title()

musico = formando_nome('jimi', 'hendrix')
print(musico)