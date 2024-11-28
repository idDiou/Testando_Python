#caso precise remover mais de uma vez o mesmo item de uma lista

animais = ['gato', 'cachorro', 'gato', 'gato', 'napoleão', 'goblin', 'mamute', 'gato', 'peixe', 'besouro']
contagem = 1

for animal in animais:
    if animal == 'gato':
        contagem +=1
    if contagem > 1:
        contagem = 1
        if animal == 'gato':
            animais.remove(animal)
    print(contagem)

print(animais)

#código para deixar apenas um gato na lista