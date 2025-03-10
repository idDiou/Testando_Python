#igual ao anterior mas dessa vez utilizaremos o método pass para que python falhe em silencio


def contando_palavras(filename):
    try:
        with open (filename, encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            lista = conteudo.split()
            contagem = len(lista)
            print(conteudo, '\n\neste foi todo o livro de alice no pais das maravilhas em inglês.')
            print('ele possui ' + str(contagem) + ' palavras')
    except:
        pass

while True:
    arquivo_rev = input('Diga um arquivo que irei procurar ele para você!\nOU\nDiga SAIR\n')
    if arquivo_rev == 'sair' or arquivo_rev == 'SAIR':
        break
    else:  
        contando_palavras(arquivo_rev)
