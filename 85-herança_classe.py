import Carro

class EletricCar(Carro.Car):
    """cria um carro só que elétrico"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = 70
    def desc_bateria(self):
        print('este carro tem ' + str(self.bateria)+'-kWh de bateria.')
    def combustivel(self):
        print('este carro é movido a energia elétrica, não precisa de gasolina.')

my_tesla = EletricCar('Tesla', 'Model S', '2016')

print(my_tesla.get_desc())

EletricCar.desc_bateria(my_tesla)
EletricCar.combustivel(my_tesla)