#reescrever o exercicio de glossário do arquivo 33 utilizando a função OrderedDict da blioteca collection
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['Joaquim'] = 'Ruby'
favorite_languages['Cosmo'] = 'Java'
favorite_languages['Henrique'] = 'C'
favorite_languages['Igor'] = 'Css'
favorite_languages['Junior'] = 'Css'
favorite_languages['Robert'] = 'Java'

for nome, linguagem in favorite_languages.items():
    print('a linguagem favorita de ' + nome.title() + 'é ' + linguagem.title() + '!')