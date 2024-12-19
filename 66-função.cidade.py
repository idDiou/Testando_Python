#escreva uma função que aceite o nome de uma cidade de seu país
#a função deve exibir uma frase simples
#como "Raykjavik está localizada na islandia"
#forneça um vaçpr default ao parametro que representa o país
#chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default

def cidades(cidade, pais='Brasil'):
    print('a cidade de '+cidade+' está localizada no seguinte país: '+pais)

cidades('porto alegre')
cidades('maranhão')
cidades('berlim', 'alemanha')