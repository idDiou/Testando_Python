#cria uma classe chamada restaurante
#o método __init__ deve armazenar dois atributos: nome e tipo
#crie um método chamado descrição_restaurante que exiba essas duas informações
#crie um método chamado open_restaurant que exiba uma mensagem informando que o restaurante está aberto.
#crie uma instância a partir de sua classe e em seguida chame os dois métodos

class Restaurante():
    """modelando um restaurante"""
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    def desc(self):
        print('este é o ' + self.nome.title() + ' um restaurante que serve ' + self.tipo.title()) 
        Restaurante.open()
    def open(self):
        print('**portas se abrindo**')
        print('o ' + self.nome.title()+ ' está com as portas abertas.')


comida1 = Restaurante('Akibaba', 'Comida Arábe')

comida1.desc()


print('\n')

comida2 = Restaurante('Kalzone', 'Pastéis Assados')

comida2.desc()
