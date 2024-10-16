Lista_Pessoas = {'Roberto':'C++', 'Joaquim':'Ruby', 'Cosmo':'Java', 'Henrique': 'C', 'Igor':'Css', "Junior":'css', 'Robert': 'Java'}
Responderam = ['Igor', 'Henrique', 'Joaquim']

for teste in set(Lista_Pessoas.keys()):
    if teste in Responderam:
        print('Obrigado', teste, 'por responder')
    if teste not in Responderam:
        print(teste, 'você ainda não respondeu a enquete, poderia responder?')