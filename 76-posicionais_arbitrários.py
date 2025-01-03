#se quiser que uma função aceite vários tipos de argumentos
#deve corresponder na ordem correta deles tais como:

#na definição da função python armazena o primeiro valor recebido em "tamanho"
#todos os demais valores que vierem depois são armazenados na tupla "*toppings"
def make_pizzas(Tamanho, *toppings):
    print('--fazendo uma pizza de tamanho '+Tamanho +', com os seguintes ingredientes--')
    for ingredientes in toppings:
        print('*'+ingredientes +'*')
make_pizzas('grande', 'pepperoni')
make_pizzas('pequena','mushrooms', 'pimentão', 'queijo extra')