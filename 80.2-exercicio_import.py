#usando um programa que você tenha escrito e que contenha uma unica função armazene essa função em um arquivo separado
#importe a função para o arquivo principal de seu programa e chame-a usando cada uma das seguintes abordagens:

#import nome_do_modulo 

#from nome_do_módulo import nome_da_função

#from nome_da_função as nf

#import nome_do_modulo as nm

#from nome_do_modulo import *

import ola

ola.ola(['dio'])

usuarios = ['Grinch', 'Pelé', 'Rocambole']

ola.ola(usuarios)


from cidades2 import city
city()
from cidades2 import city as nf
nf()

import ola as oi

oi.ola(['katoryn'])