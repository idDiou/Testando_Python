from testando_func import formando_nome

first = input('Sistema: me diga seu primeiro nome\nmongol: ')
last = input('Sistema: e seu sobrenome?\nmongol: ')

nome = formando_nome(first, last)

print(nome)