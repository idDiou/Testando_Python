#para um programa que deva executar somente enquanto muitas condições forem verdadeiras, podemos definir uma variável
#que determina se o programa como um todo deve estar ativo. essa variavel, chamada de flag, atua como um sinal para o
#programa, podemos escrever nossos programas de modo que executem enquanto a flag estiver definida como TRUE.
#e parem de executar quando qualquer um dos vários eventos definir o valor de flag para FALSE.
#como resultado nossa instrução while precisa apenas verificar uma condição: se a flag, no momento, é True ou False.

prompt = "\nDiga-me alguma coisa e eu vou repetir pra você"
prompt += "\nDigite 'quit' para finalizar o programa.\n"
active = True

while active:
    mensagem = input(prompt)
    
    if mensagem == 'quit':
        active = False
        print('fim do programa')
    elif mensagem != 'quit':
        print('toma aqui sua mensagem:', mensagem)