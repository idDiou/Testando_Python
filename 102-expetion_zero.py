#criar uma calculadora com numeros de divisão

print('me dê dois numeros, que irei dividir eles\nou digite "q" para sair.')

while True:
    num1 = input('primeiro numero: ')
    num2 = input('segundo numero: ')
    if num1 == 'q':
        break
    if num2 == 'q':
        break
    try:
        dividir = int(num1)/int(num2)
        print('o resultado é: ' + str(dividir))
    except ZeroDivisionError:
        print('não é possível dividir por zero o abobado')