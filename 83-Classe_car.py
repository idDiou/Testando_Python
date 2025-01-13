class Car():
    """uma tentativa simples de representar um carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometro = 0
    def get_desc(self): 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def kmtragem(self):
        print('esse carro rodou ' + str(self.odometro) + '|KM, até o momento.')

new_car = Car('audi', 'A4', '2016')

print(new_car.get_desc())

#uma das formas de alterar um atributo é referenciado ele dessa forma, na linha 7 ele é 0 por padrão na classe
#mas abaixo consegui alterar ele para 23 conforme necessidade.
new_car.odometro = 23
new_car.kmtragem()

#mas também é possível alterar com um método, como farei no próximo exercício o 83.2