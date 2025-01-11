#função para importar no exercicio 80.2
cidade_pais = {}
ativo = True
def city_discovery():
    while ativo:
        cidade1 = input('digite sua cidade: ')
        if cidade1 == 'q':
            cidade = 'none'
            pais = 'none'    
            ativo=False
        elif cidade1 != 'q':
            cidade = cidade1
            pais1 = input('digite seu pais: ')
            if pais1 == 'q':
                pais = 'none'
                ativo=False
            elif pais1 != 'q':
                pais = pais1   
        cidade_pais[cidade] = pais
        while resposta != 'Y' or resposta != 'N':
            resposta = input('deseja adicionar mais algum local? Y or N')
            if resposta == 'Y':
                print('perfeito, vamos começar de novo então/\n')
            elif resposta == 'N':
                for city, country in cidade_pais.items():
                    print(city,'é um lugar muito bom de se viver e o clima de', country,'é muito agradável')
                ativo=False

#programa não funcionou como esperado, tentei outra versão no cidades2
city_discovery()