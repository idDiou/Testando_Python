lugares = ['noruega', 'canadá', 'japão', 'alemanha', 'reino unido']

#pegando os 3 primeiros da lista
print('esse é os 3 primeiros da minha lista', lugares[:3])

#pegando os 3 ultimos da lista
print ('esse é os ultimos 3', lugares[-3:])

#testando clonagem de lista
pizzas = ['calabresa', 'alho-poró', '4 queijos', 'strogonoff', 'lombo canadense']
#é necessário definir o inicio/final da lista pra que seja um clone, caso não haver essa definição o python entende que
#são duas variaveis se referindo para uma mesma lista, o que acarreta em erros
friend_pizza = pizzas[1:]

pizzas.append('Salamito')

print ('Eu amo essas pizzas:')
for pizza in pizzas:
    print (pizza)

print ('-Mas meu amigo ama essas-')
for pizza in friend_pizza:
    print(pizza)

