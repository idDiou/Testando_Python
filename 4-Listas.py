#Parte 1, lista
print ('parte 1')
names = ['katlyn', 'Dio', 'Antonio',]
print ('ola ', names[0],'Eu te amo')
print ('ola ', names[1],'Eu te amo')
print ('ola ', names[2],'Eu te amo')

#parte 2
print('parte 2')
coisas = ['Pc-Gamer', 'BMW',]
print('eu terei:',coisas[0],coisas[1])

#Parte 3, inserindo 
names.insert(0, 'Cleiton')
print(names)

#parte 4, removendo da lista
del names[0]
print (names)

#parte 5,  fazer um pop, tirar o item de "cima da pilha"
popped_names = names.pop()
print (names)
print (popped_names)
linda = 'katlyn'
names.remove(linda)
print (names)