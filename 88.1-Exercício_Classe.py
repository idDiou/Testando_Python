#Admin
#Um administrador é um tipo especial de usuário
#escreva uma classe chamada admin
#que herde a classe User escrita no exercicio 9.3
#adicione um atributo chamado "privilegios"
#que armazene uma lista de strings como "Pode postar", "pode deletar post", "pode Banir usuário", etc.
#escreva um método chamado "Mostrar_privilegios()", que liste o conjunto de privilégios de um administrador
#crie uma instância de admin e chame seu método

class Users():
    def __init__(self, nome, login, poderes):
        self.nome = nome
        self.login = login
        self.poderes = poderes
        self.priv = []
        Users.privilegios(self)
    def desc(self):
        print('Nome: ' + self.nome)
        print('Login:' + self.login)
        print('poderes: ' + self.poderes)
    def privilegios(self):
        self.priv = ['Pode postar', 'Pode alterar própria senha', 'Pode apagar os próprios posts']
    def desc_priv(self):
        print('O seguinte ' + self.poderes + ' detém os seguintes privilégios: ')
        for power in self.priv:
            print('*' + power)
    def hello(self):
        print('Ola ' + self.nome + '! ou devo dizer ' + self.login + '? fico feliz que seu jogo favorito seja o ' + self.jogo)

class Admin(Users):
    def __init__(self, nome, login, poderes):
        super().__init__(nome, login, poderes)
        Admin.privilegios(self)
    def privilegios(self):
        self.priv = ['Pode postar', 'Pode alterar qualquer senha', 'Pode apagar qualquer post', 'Pode banir']

dio = Admin('Dionata', 'DioApenas', 'admin')
kat = Users('Katoryn', 'KatGatinha123', 'Usuário')

dio.desc()
dio.desc_priv()