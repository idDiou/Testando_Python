#criando método para alterar a kilometragem
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
    def update_km(self, mileage):
        self.odometro = mileage

new_car = Car('audi', 'A4', '2016')

print(new_car.get_desc())


new_car.update_km(23)
new_car.kmtragem()