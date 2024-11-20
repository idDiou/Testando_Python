#uma ferramente util para trabalhar com informações numéricas é o operador de módulo (%), que divide um numero por outro
#e devolve o resto

A = 4 % 3

B = 5 % 3

C = 7 % 3

D = 23 % 20

print('o resulado de A:', A)
print('o resulado de B:', B)
print('o resulado de C:', C)
print('o resulado de D:', D)

#Esse operador de módulo não diz quantas vezes um numero cabe em outro; ele simplesmente informa o resto.
#quando um numero é divisivel por outro, o resto é 0.

#portanto o operador de módulo sempre devolve 0, nesse casom oidenis ysar esse fato para determinar se um numero é par ou impar.

numero = input('Escreva um numero e direi se ele é par ou impar: ')
numero = int(numero)

if numero % 2 == 1:
    print('Seu numero é impar')
elif numero % 2 == 0:
    print('Seu numero é par')