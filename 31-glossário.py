glossario = {'laço': 'utilizado para criar uma espécie de looping até que determinada condição seja realizada.' ,
             'If':'utilizado para verificar determinada condição, uma espécie de "se", se tal condiçao for verdadeira realizar tal coisa ou se tal condição for falsa realizar tal coisa' ,
             'for':'utilizado para criar laços, enquanto determinada condição for verdadeira ou falsa' ,
             'lista': 'utilizada para armazenar muitas informações' ,
             'tuplas': 'muito parecida com as listas, porém seus valores são imutáveis',}
print('nesse modulo aprendemos muitas coisas destaco as mais importantes: ', '\n')

#não utilizar o sinal de positivo em dicionários, apenas virgulas vão funcionar


for palavras in glossario:
    if palavras == 'laço':
        print ('Laço:')
        print(glossario['laço'], '\n')
    if palavras == 'If':
        print ('If:')
        print(glossario['If'], '\n')
    if palavras == 'for':
        print ('for:')
        print(glossario['for'], '\n')
    if palavras == 'lista':
        print ('lista:')
        print(glossario['lista'], '\n')
    if palavras == 'tuplas':
        print ('tuplas:')
        print(glossario['tuplas'], '\n')