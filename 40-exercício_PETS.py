#Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação. 
#em cada dicionário, inclua o tipo de animal e o nome do dono.
#armazene esses dicionários em uma lista.
#apresente tudo que você sabe sobre cada animal.

PETS = {'Gato de Botas':{'Tipo':'Gato', 'Sexo':'Masculino', 'Arma': 'espada'}, 'Morte':{'Tipo': 'Lobo', 'Sexo:':'Masculino', 'Arma': 'Foice/Lamina Curva'},
        'Perrito':{'Tipo':'Cachorro', 'Sexo':'Masculino', 'Arma': 'Gentileza'}, 'Kitty':{'Tipo':'Gato', 'Sexo':'Feminino', 'Arma': 'espada'},
        'Cachinhos':{'Tipo':'Humano', 'Sexo':'Feminino', 'Arma': 'Bastão/Ursos'}}

print('assisti o filme Gato de Botas 2 e nele vi personagens muito legais, alguns se destacam por algumas coisas tais como: ')
for nome, info in PETS.items():
        print(nome)
        print('é um', info['Tipo'], 'e utiliza', info['Arma'], 'Como arma')
    