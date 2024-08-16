carros = ['audi', 'bmw', 'subaru', 'toyota']

#utilizando laço for e if para que apenas a BMW seja escrita toda em maiusculo
for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())

teste = ('mel')

# != serve se quiser determinar se dois valores não são iguais
if teste != 'amendoim': #se o "teste" não for igual a amendoim essa instrução será executada pelo python
    print ('não é amendoim') #pois retorna True, caso fossem iguais retornaria o valor False

#é possível utilizar com numeros também

idade = 18
idade == 18 #true
idade != 18 #false

if idade == 18: #true
    print ('tenho 18 anos')

if idade != 42: #true
    print('não, não tenho 42, tenho 18 mesmo')