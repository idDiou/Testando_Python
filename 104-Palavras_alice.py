#fazer um algoritmo que conte quantas palavras tem no livro da alice no pais das maravilhas

#create an algorithm to count how many words are in the book Alice in Wonderland


with open ('alice_wonderland.txt', encoding="utf-8") as alice:
    conteudo = alice.read()
    lista = conteudo.split()
    contagem = len(lista)
    print(conteudo, '\n\neste foi todo o livro de alice no pais das maravilhas em inglês.')
    print('ele possui ' + str(contagem) + ' palavras')

