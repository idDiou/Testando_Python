#Tentativas de Login
#acrescente um atributo referente a tentavivas de login na clase User do exercicio 82.2
#escreva um método que incremente o valor do método anterior em 1
#escreva outro método que reinicie o valor de volta para zero
#teste várias vezes para garantir que tudo está funcionando corretamente

contagem = {}
#criei uma lista para que a contagem não se perdesse

class Users():
    def __init__(self, nome, usuario, jogo, login):
        self.nome = nome
        self.usuario = usuario
        self.jogo = jogo
        self.login = login
    def desc(self):
        print('Nome: ' + self.nome)
        print('Login:' + self.usuario)
        print('Jogo: ' + self.jogo)
    def hello(self):
        print('Ola ' + self.nome + '! ou devo dizer ' + self.usuario + '? fico feliz que seu jogo favorito seja o ' + self.jogo)
    #método para criar lista abaixo
    def conta_log(self):
        contagem[self.nome] = self.login
    #método para alterar lista abaixo
    def logar(self):
        Users.conta_log(self)
        tentativa = 1
        for pessoa, numero in contagem.items():
            if pessoa == self.nome:
                soma = numero + tentativa
                contagem[self.nome] = soma
                self.login = soma
                print('fazendo a tentativa N|' + str(self.login))
    #método para resetar lista
    def reset(self):
        self.login = 0
        contagem[self.nome] = self.login

usuario1 = Users('Dio', 'NightRex', 'Age of Empires', 0)

usuario2 = Users('Henrique', 'Daaparty', 'Brawhalla', 0)

usuario2.logar()
usuario2.logar()
usuario2.logar()
usuario2.logar()
usuario2.reset()

print(contagem)

