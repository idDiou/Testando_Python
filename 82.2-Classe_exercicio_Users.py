#crie uma classe chamada users
#crie dois atributos normalmento armazenados em um perfil de usuário.
#escreva um método de descrição que apresente um resumo das informações do usuário
#outro método para apresentar uma saudação personalizada ao usuário

class Users():
    def __init__(self, nome, login, jogo):
        self.nome = nome
        self.login = login
        self.jogo = jogo
    def desc(self):
        print('Nome: ' + self.nome)
        print('Login:' + self.login)
        print('Jogo: ' + self.jogo)
    def hello(self):
        print('Ola ' + self.nome + '! ou devo dizer ' + self.login + '? fico feliz que seu jogo favorito seja o ' + self.jogo)


usuario1 = Users('Dio', 'NightRex', 'Age of Empires')

usuario1.desc()
usuario1.hello()

usuario2 = Users('Henrique', 'Daaparty', 'Brawhalla')

usuario2.desc()
usuario2.hello()