#Lista de Convidados

#escreva um laço while que pergunte o nome aos usuários
#quando fornecerem seus nomes, apresente uma saudação na tela  
#acrescente uma linha que registre a visita do usuário em um arquivo chamado guest_book.txt
#certifique-se que cada entrada esteja em uma nova linha do arquivo
numero_linha = 1

while True:
    with open('guest_list.txt','r', encoding="utf-8") as arquivo:
        numero_lista = arquivo.readlines()
        numero = numero_lista[1]
        numero_c = int(numero) + 1
        numero_lista[1] = numero_c
    
    nome = input('HELLOOOOOOOOOOO, convidado N-' + str(numero_c) + ' qual o seu nome?\n')    
    if nome == 'cancel':
        break
    print('OH OLA ' + nome + ' BEM VINDO AO MARTErBURGUER, O MELHOR HAMBURGUER DA GAKAlaXIA, HA HA HA!')
    pedido = input('o que você gostaria hoje?\n')
    if pedido == 'cancel':
        break
    
    with open('guest_list.txt', 'a', encoding="utf-8") as lista_visitas:
        lista_visitas.write('\nNome:' + nome + '\nPedidos: ' + pedido +'\n')
        lista_visitas.write('Convidado numero: ' + str(numero_c) + '\n')
    
    with open('guest_list.txt','r', encoding="utf-8") as final:
        conteudo = final.readlines()
        conteudo[1] = str(numero_c) + '\n'
        conteudo[2] = '----------------------------------------------------------------------------------------------'
    
    with open('guest_list.txt','w', encoding="utf-8") as final:
        final.writelines(conteudo)