alfabeto = ['morto',"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
decisao = int(input('Digite um numero\n'))


if 1 <= decisao <= 25:
    print('a letra escolhida é: ')
    print(alfabeto[decisao])

else:
    print('numero invalido')