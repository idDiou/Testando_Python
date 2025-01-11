#para o exercicio 80.2
def city():
    locais = {}
    ativo = True
    while ativo:
        cit = input('digite sua cidade: ')
        country = input('digite o pais dessa cidade: ')
        locais [cit] = country
        repeat = input('se quiser armazenar outro local digite "Y": ')
        if repeat == 'Y' or repeat == 'y':
            print('perfeito vamos começar de novo\n')
        else:
            ativo = False
    
    print('resultado do armazenamento: \n')
    for cidade, pais in locais.items():
        print('*' + cidade, 'é um ótimo local para se viver e', pais, 'tem um clima muito agradável\n')

city()