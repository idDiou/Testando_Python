#Sorveteria
#Uma sorveteria é um tipo especifico de restaurante.
#escreva uma classe chamada Sorveteria
#que herde a classe restaurante do exercicio anterior
#qualquer versão da classe funcionará; basta escolher aquela que você mais gosta
#adicione um atributo chamado "Sabores", que armazene uma lista de sabores de sorvete
#escreva um método para mostrar esses sabores
#crie uma instancia de "Sorveteria" que chame esse método

#classe restaurante
class Restaurante():
    """modelando um restaurante"""
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    def desc(self):
        print('este é o ' + self.nome.title() + ' um restaurante que serve ' + self.tipo.title()) 
    def open(self):
        print('**portas se abrindo**')
        print('o ' + self.nome.title()+ ' está com as portas abertas.')


class Sorveteria(Restaurante):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        sabores = ['morango', 'Chocolate', 'Amendoim', 'Caju', 'Feijones']
        self.sabores = sabores
    def desc_sabores(self):
        print('Bem vindo ao ' + self.nome + ' somos empenhados em servir o melhor sorvete da cidade\nTemos os seguintes sabores:')
        for sabor in self.sabores:
            print('*' + sabor)

cremolato = Sorveteria('Cremolato', 'Sorveteria')

cremolato.desc_sabores()