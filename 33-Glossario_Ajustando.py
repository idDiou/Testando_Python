favorite_languages = {'Roberto':'C++', 'Joaquim':'Ruby', 'Cosmo':'Java', 'Henrique': 'C', 'Igor':'Css', "Junior":'css', 'Robert': 'Java'}
Amigos = ['Igor', 'Henrique']

#cita apenas os nomes que estejam em ambas as listas acima
for nome in favorite_languages.keys():
    if nome in Amigos:
        print('Olá', nome.title(), 'fico feliz que você goste de', favorite_languages[nome].title() + '!')

#verifica se Erin está ou não na lista e por não estar, ativa a função
if 'Erin' not in favorite_languages:
    print('Venha, escolher sua linguagem favorita Erin')

#o Value utilizado após a lista tem a função de puxar apenas os valores das chaves de cada glossario
for linguagem in favorite_languages.values():
    print(linguagem)

print('--------------------------------------------------------------------------------------------------------------------------------------------------')

#método Set utilizado para que nenhum valor se repita
for langyage in set(favorite_languages.values()):
    print(langyage)