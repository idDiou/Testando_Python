#DADOS

#o módulo Random contém funções que geram numeros aleatórios
#a função randit() devolve um numero inteiro no intervalo especificado por você
#o código a seguir devolve um numero entre 1 e 6
#x = randit(1,6)
#crie uma classe Die com um atributo chamado sides, cujo valor default é 6
#escreva um método chamado roll_die(), que exiba um numero aleatório entre 1 e os lados do dado
#crie um dado de seis lados
#crie um dado de dez lados e outro de vinte lados
#lance cada dado dez vezes

from random import randint

class Dados():
    def __init__(self, lados = 6):
        self.lados = lados
    def rolar(self):
        print('rolando dado de ' + str(self.lados) + ' lados'+ '...')
        valor = randint (1, self.lados)
        print('|' + str(valor) + '|')

dado1 = Dados()
dado2 = Dados(10)
dado3 = Dados(20)

dado1.rolar()
dado2.rolar()
dado3.rolar()