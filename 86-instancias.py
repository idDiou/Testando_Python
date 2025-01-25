#ao modelar algo do mundo real você poderá perceber que está adicionando cada vez mais detalhes em uma classe.
#poderá notar que há uma lista crescente de atributos e métodos e que seus arquivos estão começando a ficar extensos.
#nessas situações, talvez você perceba que parte de uma classe pode ser escrita como uma classe separada.
#sua classe maior poderá ser dividida em partes menores que funcionem em conjunto.

#por exemplo, se continuarmos adicionando detalhes à classe EletricCar, podemos perceber que estamos acrescentando
#muitos atributos e métodos a bateria do carro. se percebermos que isso está acontecendo, podemos parar e transferir
#esses atributos para uma classe diferente, chamada "Bateria()", então podemos usar uma instancia de bateria como um
#atributo da classe "EletricCar().