#utilize o exercicio anterior
#use o método replace() para substituir uma palavra
#substitua o python por C

with open('aprendendo_python.txt', encoding="utf-8") as arquivo:
    info_list = arquivo.readlines()
    

contagem = 1

for conteudo in info_list:
    print(str(contagem)+ '-' + conteudo.replace('python', 'C'))
    contagem += 1