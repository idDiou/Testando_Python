#Carros

#escreva uma função que armazene informações sobre um carro em um dicionário
#a função sempre deve receber o nome do fabricante e um modelo
#um numero arbitrário de argumentos deve ser aceito
#chame a função com as informações necessárias e dois outros pares nome-valor
#por exemplo: uma cor, ou um opcional
#sua função deve ser apropriada para uma chamada como esta:
#car = make_car['Subaru', 'outback', color = 'blue', tow_package= True]

def Carros(Marca, Carro, low_package=False,  **caracteristicas):
    Me = {}
    Me['Marca_Carro'] = Marca
    Me['Carro'] = Carro
    if low_package == True:
        print('um carro popular:')
    else:
        print('um carro de luxo:')
    print('\num', Carro,'da marca', Marca,'essas são as especificações:')
    for key,value in caracteristicas.items():
        Me [key] = value
        print('\n*'+key +':\n')
        for chave in value:
            print('-'+chave)


Carros('Subaru', 'Outback', cor = ['Azul'], tipo = ['corrida'])

Carros('Chevrolet', 'Celta', cor=['preto'], tipo = ['turbo'], low_package=True)