#crie uma lista para colocar os sanduiches
#preencha a lista com os nomes de vários sanduíches
#crie outra lista chamada sanduíches finalizados
#percorra a lista de pedidos de sanduíches com um laço e mostre uma mensagem para cada pedido
#transfira os pedidos para a lista de sanduíches prontos
#mostre uma mensagem que mostre os sanduiches prontos

#usando a o mesmo exercicio garanta que o sanduiche de pastrami apareça na lista pelo menos três vezes
#acrescente um código próximo ao inicio de seu programa para exibir uma mensagem informando que a lanchonete está sem pastrami
#então use um laço while para remover todas as ocorrências de pastrami

pedidos = []
prontos = []
sanduiches_finalizados = []
ativo = True
contagem = 0
print('*********************************************************')
print('*****************bem vindo ao SimSaudich*****************')
print('*********************************************************')
while ativo:
    sanduiches = input('qual vai ser o pedido?\n')
    if sanduiches == 'sanduiche de pastrami':
        print('infelizmente não temos pastrami')
    pedido = (sanduiches)
    pedidos.append(pedido)
    resposta = input('gostaria de pedir algo mais? Y or N\n')
    if resposta == 'N' or resposta == 'n':
        ativo = False

for sanduiche in pedidos:
    contagem = int(contagem)
    contagem += 1
    contagem = str(contagem)
    print('o pedido N'+contagem+':', sanduiche,'está sendo preparado...' )
    for valor in range (1,11):
        valor = str(valor)
        print(valor+'...')
        valor = int(valor)
    print('seu', sanduiche,'está pronto!')
    sanduiches_finalizados.append(sanduiche)

while 'sanduiche de pastrami' in sanduiches_finalizados:
    sanduiches_finalizados.remove('sanduiche de pastrami')

print('os sanduiches finalizados:')
for pao in sanduiches_finalizados:
    print(pao)