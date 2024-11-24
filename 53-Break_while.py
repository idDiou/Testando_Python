#para interromper um laço while a qualquer momento, utilize a função break

prompt = '\ndigite o nome de um local que você já visitou\n'
prompt += "digite 'quit' para encerrar o programa\n"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print('eu amo', city.title() + '!')