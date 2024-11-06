#é possível armazenar uma lista em um dicionário da seguinte forma:
lista = {'katoryn':['portugues', 'alemão', 'japonês'], 'Dio':['português', 'inglês', 'Python'], 'antonio': ['biruleixo']}
feminino = ['katoryn']
for name, linguagem in lista.items():
    if name in feminino:
        print ('a linguagem da', name.title(), 'é:')
    for linguage in linguagem:
        print(linguage)
    if name not in feminino:
        print ('a linguagem do', name.title(), 'é:')
        for linguage in linguagem:
            print(linguage)