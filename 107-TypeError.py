#tratar um erro de tipo
#comum quando o usuário fornece textos ao invés de numeros
#ao tentar convertar a entrada para um int, você obterá um TypeError
#escreva um programa que peça dois numeros ao usuário
#some-os e mostre o resultado
#capture o TypeError caso algum dos valores de entrada não seja um numero
#apresente uma mensagem de erro simpática
#teste seu programa
while True:
    try:
        num1 = input('vamos somar numeros? digite o primeiro: ')
        if num1 == 'sair':
            break
        num2 = input('agora digite o segundo: ')
        num3 = int(num1) + int(num2)
        print('SOMA: ' + str(num3))
    except ValueError:
        print('EU PEDI NUMERO SEU ANIMAL, NÃO PALAVRAS ARRRRGH')