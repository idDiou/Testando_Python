alien_0 = {'cor': 'verde', 'pontos': '10' }
alien_1 = {'cor': 'rosa', 'pontos': '5' }
alien_2 = {'cor': 'azul', 'pontos': '1' }

aliens = []
#criando lista com 10 aliens de cada
for numero_aliens in range(31):
    if numero_aliens <= 9:
        aliens.append(alien_0)
    if numero_aliens <= 19 and numero_aliens > 9:
        aliens.append(alien_1)
    if numero_aliens <=29 and numero_aliens > 19:
        aliens.append(alien_2)


print('LISTA 1')
print(aliens)
print('numero total de alienigenas:', str(len(aliens)))

for alien in aliens[0:5]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['pontos'] = 20

print('LISTA 2')
print(aliens)