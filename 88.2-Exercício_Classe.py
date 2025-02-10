#pegue o exercicio passado e escreva uma classe "Privileges" separada.
#a classe deve ter um atributo privileges que armazene uma lista de strings conforme descrita no exercicio anterior
#e um método para demonstrar esses privilégios

class Users():
    def __init__(self, nome, login, poderes):
        self.nome = nome
        self.login = login
        self.poderes = poderes
        self.priv = []
    def desc(self):
        print('---------------------------------------\n' +'Nome: ' + self.nome)
        print('Login: ' + self.login)
        print('poderes: ' + self.poderes)
    def desc_priv(self):
        print( self.login + ' possui os seguintes privilégios:')
        self.priv = Privilegios(numero = 2)

    def hello(self):
        print('Ola ' + self.nome + '! ou devo dizer ' + self.login + '? fico feliz que seu jogo favorito seja o ' + self.jogo)


class Admin(Users):
    def __init__(self, nome, login, poderes):
        super().__init__(nome, login, poderes)
        self.priv = []
    def desc_priv(self):
        print(self.login + ' possui os seguintes privilégios:')
        self.priv = Privilegios(numero = 1)

class Privilegios():
    def __init__(self, numero):
        self.numero = numero
        Privilegios.teste(self)
    def teste(self):
        if self.numero == 1:
            Privilegios.adm_priv(self)
        elif self.numero == 2:
            Privilegios.user_priv(self)
    def adm_priv(self):
        self.priv = ['Pode postar', 'Pode alterar qualquer senha', 'Pode apagar qualquer post', 'Pode banir']
        Privilegios.desc_privl(self)
    def user_priv(self):
        self.priv = ['Pode postar', 'Pode alterar própria senha', 'Pode apagar os próprios posts']
        Privilegios.desc_privl(self)
    def desc_privl(self):
        for poderes in self.priv:
            print('*/' + poderes)


dio = Admin('Dionata', 'DioApenas', 'admin')
kat = Users('Katoryn', 'KatGatinha123', 'Usuário')

dio.desc()
dio.desc_priv()

kat.desc()
kat.desc_priv()