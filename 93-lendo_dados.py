#repetindo do exercicio 91

#método redlines armazena cada linha de um arquivo em uma lista
with open ('pi.txt') as conteudo_arquivo:
    lines  = conteudo_arquivo.readlines()

for line in lines:
    print(line.strip())
