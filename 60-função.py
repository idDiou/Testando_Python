#quando queremos executar uma tarefa em particular, definida em uma função, chamamos o nome da função responsável por ela

def greet_user(username): 
    """função de saudação""" #docstring, feita com aspas triplas
    print('hello, ' + username.title()+'!')

#a função aceita o nome que for passado e exibe a saudação para esse nome
greet_user('jesse') #chama a função
greet_user('amendoim')

#jesse é um exemplo de argumento.
#um argumento é uma informação passada para uma função em sua chamada.
#colocamos entre parenteses o valor que queremos que ela trabalhe
