prompt = "\nDiga-me alguma coisa e eu vou repetir pra você"
prompt += "\nDigite 'quit' para finalizar o programa.\n"

message = ""
#algoritimo para finalizar o laço quando a palavra quit for escrito
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print('tome a repetição:', message)
    elif message == 'quit':
        print('Fim do Programa')