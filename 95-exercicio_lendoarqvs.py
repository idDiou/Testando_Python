#abra um arquivo em branco
#escreva algumas linhas que sintetizem o que aprendeu em python até agora
#comece cada linha com "em python podemos..."
#exiba o conteúdo uma vez lendo todo o arquivo
#outra percorrendo o objeto do arquivo com um laço

with open('aprendendo_python.txt', encoding="utf-8") as arquivo:
    info_list = arquivo.readlines()

info = ''
for texto in info_list:
    info += texto
print(info)

contagem = 1

for conteudo in info_list:
    print(str(contagem)+ '-' + conteudo)
    contagem += 1