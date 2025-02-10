#Convidado
#escreva um programa que pergunte o nome ao usuario
#quando ele responder, escreva o nome em um arquivo chamado guest.txt

lista_nomes = 'guest.txt'

nome = input('qual o seu nome?\n')

with open ('guest.txt', 'a') as save_name:
    save_name.write(nome+'\n')