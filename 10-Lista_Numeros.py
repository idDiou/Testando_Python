#range é utilizado para contar os numeros dentro de um intervalo
#range inicia no valor indicado e termina um valor abaixo
for valor in range(1,5):
    print (valor)

#usando range para criar lista de numeros
numeros = list(range(1,6))
print (numeros)

#lista de numeros pares
numeros_pares = list(range(2,11,2)) #o dois no final é pra indicar que a lista
print (numeros_pares)               #vai somar de 2 em 2

multiplos = []
for valorr in range (1,11): #laço for, o codigo percorre os valores de 1 a 10
    multiplo = valorr**2    #o valor é elevado ao quadrado
    multiplos.append(multiplo) #tira o valor de multiplo e grava na lista

print (multiplos)              #escreve a lista

digitos = [1,2,3,4,5,6,7,8,9,0]
print (min(digitos)) #o menor valor
print (max(digitos)) #o maior valor
print (sum(digitos)) #a soma dos valores

#gerando diretamente dentro da lista, não se utilizam os ':' dentro da lista
lista_quadrados = [valor**2 for valor in range (1,11)]
print (lista_quadrados)