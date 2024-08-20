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


diferente = 'diferenter'

if diferente == 'diferenter':
    print('true')
else:
    print('false')

if diferente == 'diogo defante':
    print('true')
else:
    print('false')

if diferente != 'diogo defante':
    print('true')
else:
    print('false')

if diferente != 'diferenter':
    print('true')
else:
    print ('false')

if diferente == 'DIFERENTER'.lower():
    print('true')
else:
    print('false')

if diferente.upper() == 'DIFERENTER':
    print('True')
else:
    print('false')

if 'violão' in coisas:
    print('tem violao')

if 4 < 5:
    print('4 é maior do que 5')

if 4 != 230 or 4 == idade:
    print ('sei la')

if 45 and 27 != 25:
    print ('é diferente')

if 50 == 62 or 24 == 4041 or 24 == 24 and 22 == 23 or 22 == 24:
    print ('é isso')
else:
    ('não é isso')