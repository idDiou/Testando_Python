#escreva uma função chamada city_country()
#que aceite o nome de uma cidade de seu país
#a função deve devolver uma string formatada assim: "Santiago, Chile"

def city_country(cidades, paises):
    cidade_pais = (cidades + ', ' + paises)
    print(cidade_pais.title())

while True:
    print('digite "q" a qualquer momento para sair do programa')
    print('digite a Cidade e o Pais:')

    cidade = input('cidade: ')
    if cidade == 'q':
        break
    pais = input('pais: ')
    if pais == 'q':
        break
    
    city_country(cidade, pais)