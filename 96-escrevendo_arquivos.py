filename = 'programando.txt'

#o 'w' diz a python que queremos abrir ele em modo de escrita
#e o write diz o que escrever
with open(filename, 'w') as objeto:
    objeto.write('eu amo programar\n')
    objeto.write('eu amo criar novos jogos')

#o modo de escrita apaga o arquivo e cria um novo com os dados fornecidos

#se quiser manter os arquivos é necessário abrir em modo de concatenação
