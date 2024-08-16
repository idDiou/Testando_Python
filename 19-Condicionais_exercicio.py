coisas = ['violão', 'long', 'vassoura', 'Amendopã']

idade = 22

if 'violão' in coisas:
    print('há um violão em casa')
else:
    print('não há violão')

print ('Locutor: você tem 45 anos?')
if idade != 45:
    print('Me: não, eu tenho 22')

irmãos = 8
print ('Locutor: você tem 14 irmãos?')
if irmãos == 14:
    print('Me: Sim tenho 14 irmãos')
else:
    print('Me: na verdade tenho 8')

reposta = True

print ('locutor: quais coisas você tem em casa?')

if reposta == True:
    print('Me: Tenho coisas muito legais tais como:')
    for coisa in coisas:
        print(coisa)

print ('Locutor: Você tem mais de 2000 amigos?')
amigos = 5

if amigos != 2000:
    print('Me: não, na realidade eu tenho apenas 5')

print ('Locutor: Você tem um ralador de queijo em casa?')

if not'ralador' in coisas:
    print('Me:não tenho ralador')

print('Locutor:você gosta de contar?')
resposta1 = ('Sim')
print('me:', resposta1)
print('Locutor:Você conta até 20 pra mim?')
resposta2 = ('Sim')
print('me:', resposta2)

if resposta1 == 'Sim' and resposta2 == 'Sim':
    for contagem in range(1,21):
        print(contagem)

grito = 'GRITANDO'

if grito.lower() == 'gritando':
    print('grita baixo')
else:
    print(grito)
