milhao = [valor for valor in range (1,1000001)] #cria lista de um milhão de numeros
print (min(milhao))
print (max(milhao))
print (sum(milhao))

numeros_impares = list(range(1,21,2)) #numeros impares
print (numeros_impares)

multiplos_tres = [] #criação da lista pra ser usada

for tres in range(3,31,3): #multiplos de tres
    multiplos_tres.append(tres) #metodo append pra adicionar coisas a uma lista

print (multiplos_tres)


cubo = []
for valor in range(1,11):  #forma de fazer potencia de 3
    cubo.append(valor**3)

print(cubo)


cubo_alternativo = [valor**3 for valor in range(1,11)] #forma alternativa 

print (cubo_alternativo)

