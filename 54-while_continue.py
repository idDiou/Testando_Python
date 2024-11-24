#usando a instrução "continue" em um laço

numero_atual = 0

#o codigo verifica se um numero é divisivel por 2, se for, ele ignora o restante do código e reinicia 
while numero_atual < 10:
    numero_atual += 1
    if numero_atual % 2 == 0:
        continue
    print(numero_atual)