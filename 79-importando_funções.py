#importando funções de outros módulos

import pizza as mp

#o 'as' serve para renomear o chamado da função, ao invés de se chamar "pizzas", se chama mp

mp.make_pizzas('peperoni', 'Queijo', 'Molho de Tomate')

#versão sem o mp:
#pizzas.make_pizzas('peperoni', 'Queijo', 'Molho de Tomate')

#Podemos utilizar a seguinte forma para importar apenas uma função

from pizza import make_pizzas

#utilizando virgulas podemos importar várias funções

#from nome_do_modulo import função_01, função_02, função_03 


#utilizando asterisco (*) ele chama todas as funções

#from pizza import *