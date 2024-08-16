age = 19 #igual a
age < 21 #menor que
age <= 21 #menor ou igual a
age > 21 #maior do que
age >= 21 #maior ou igual a

age != 21 #é Diferente de?
age == 21 # é igual?

age_0 = 22
age_1 = 18

#"and" serve para testar dois valores, os dois precisam passar pra ser avaliado como True
age_0 >=22 and age_1 >=22 #false, pois o teste da direita falha
age_0>= 15 and age_1 >=15 #true, pois ambos passam

#para descobrir se um valor particular já está em uma lista utilize "In"
ingredientes = ['cogumelos','onions', 'abacaxi']

#verifica se há cogumelos na lista
if 'cogumelos' in ingredientes: #true
    print('há cogumelos')

#ferifica se há amendoim na lista
if 'amendoim' in ingredientes:#false
    print('há amendoim')

#caso não aja calabresa, utilizando a palavra reservada NOT
if not 'calabresa' in ingredientes: #true
    print('não há calabresa')


grito = 'GRITANDO'
#diminui a letra pra minusculo para que o teste venha como true
if grito.lower() == 'gritando':#True
    print('grita baixo')
else:
    print(grito)