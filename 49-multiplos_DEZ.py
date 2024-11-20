#peça um numero ao usuário e, em seguida, informe se o número é múltiplo de dez ou não.

numero = input('Diga um numero e te direi se ele é multiplo de dez ou não:\n')
numero = int(numero)

if numero % 10 == 0:
    print('sim, esse é um multiplo de dez')
elif numero % 10 == 1:
    print('não, esse não é um multiplo de dez')