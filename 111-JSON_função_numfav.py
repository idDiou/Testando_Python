#passar todo o código para funções

import json
info_user = {}

class NumFavorito:
    def __init__ (self):
        username = self.resposta
        filename = username.lower()+'.json'
        self.username = username
        self.filename = filename

    def pergunta(self):
        while True:
            pergunta = input('tudo bem meu amigo? qual o seu nome?\n')
            return pergunta

    def open_f(self):
        try:
            with open(self.filename) as file:
                self.info_user = json.load(file)
                print('bem vindo de volta ' + self.info_user['nome']+' seu numero favorito é o ' + self.info_user['num_fav'])
        except FileNotFoundError:
            self.cria_f()

    def cria_f(self):
        self.info_user['nome'] = self.username
        self.info_user['num_fav'] = str(input('hey ' + self.username +' vejo que é sua primeira vez por aqui ' + 'qual o seu numero favorito?\n'))
        with open(self.filename, 'w') as file:
            json.dump(info_user, file)

num_fav = NumFavorito()

num_fav.open_f()