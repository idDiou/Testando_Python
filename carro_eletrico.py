from Bateria import Battery
from carro import Car

class EletricCar(Car):
    """cria um carro só que elétrico"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Battery()
    def combustivel(self):
        print('este carro é movido a energia elétrica, não precisa de gasolina.')

tesla = EletricCar('Tesla', 'G5', '2025')

tesla.bateria.desc_bat()
tesla.bateria.get_range()

tesla.bateria.upgrade_bat(90)
tesla.bateria.desc_bat()
tesla.bateria.get_range()