#incrementando o valor de um atributo com um método
class Car():
    """uma tentativa simples de representar um carro"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometro = 5
    def get_desc(self): 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def kmtragem(self):
        print('esse carro rodou ' + str(self.odometro) + '|KM, até o momento.')
    def update_km(self, mileage):
        if mileage >= self.odometro:
            self.odometro = mileage
        else:
            print('você não pode retroceder o odometro!')
    def incrementando(self, miles):
        """soma a quantidade especificada ao valor de leitura do hodômetro"""
        self.odometro += miles

new_car = Car('audi', 'A4', '2016')

print(new_car.get_desc())


new_car.update_km(10)
new_car.kmtragem()

print('**o carro rodou 27|km**')

new_car.incrementando(27)
new_car.kmtragem()

#é possível modificar facilmente esse método para rejeitar incrementos negativos
#de modo que ninguém possa usar essa função para reduzir o valor lido no hodômetro
