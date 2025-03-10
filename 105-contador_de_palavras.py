#criar uma função que conte palavras de determinado arquivo

#create a function that counts words in a specific file"

def contando_palavras(filename):
    try:
        with open (filename, encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            lista = conteudo.split()
            contagem = len(lista)
            print(conteudo, '\n\neste foi todo o livro de alice no pais das maravilhas em inglês.')
            print('ele possui ' + str(contagem) + ' palavras')
    except:
        msg = 'não foi possível encontrar o arquivo "' + filename +'"'
        print(msg)

while True:
    arquivo_rev = input('Diga um arquivo que irei procurar ele para você!\nOU\nDiga SAIR\n')
    if arquivo_rev == 'sair' or arquivo_rev == 'SAIR':
        break
    else:  
        contando_palavras(arquivo_rev)


