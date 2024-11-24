#se usarmos a função input python sempre interpretará as entradas como strings

#Exemplo:

idade = input('qual a sua idade?')

#o usuario digita o numero 21, mas quando pedimos o valor age, python devolve '21', que é a representação em string.
#o que apresenta errros em caso de tentar fazer comparações ou calculos.

#uma forma simples de resolver isso é utilizando a função int(), que converte a representação em string de um numero
#em uma representação numérica.

age = input('quantos anos você tem?')
age = int(age)

if age >= 18:
    print(age)