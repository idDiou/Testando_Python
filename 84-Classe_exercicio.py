#comece com seu programa do exercício anterior
#acrescente um atributo chamado number_served
#cujo valor default é 0
#crie uma instancia chamada restaurant a partir dessa classe
#apresente o numero de clientes atentidos pelo restaurante 
#em seguida mude esse valor e exiba-o novamente


class Restaurante():
    """modelando um restaurante"""
    def __init__(self, nome, tipo, number_served = 0):
        self.nome = nome
        self.tipo = tipo
        self.number_served = number_served
    def desc(self):
        print('este é o ' + self.nome.title() + ' um restaurante que serve ' + self.tipo.title()) 
    def open(self):
        print('**portas se abrindo**')
        print('o ' + self.nome.title()+ ' está com as portas abertas.')
    def contagem(self, aumento = 0):
        if aumento > self.number_served:
            self.number_served = aumento
        print( '|*--' + str(self.number_served)  + ' clientes fizeram pedido no ' + self.nome.title() + '--*|')




comida1 = Restaurante('Akibaba', 'Comida Arábe')

comida1.desc()
comida1.open()

print('\n')

comida2 = Restaurante('Kalzone', 'Pastéis Assados')

comida2.desc()
comida2.open()
comida2.contagem()

print('-30 clientes atendidos\n-apenas 23 fizeram um pedido')

comida2.contagem(23)