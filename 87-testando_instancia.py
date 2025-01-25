#separando bateria da classe EletricCar, assim podemos inserir quantos métodos quisermos em bateria
#sem entulhar a classe EletricCar.

#criamos a classe bateria que não herda nenhuma outra classe
class Battery():
    """uma tentativa simples de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def desc_bat(self):
        print('este carro tem ' + str(self.battery_size)+'-kWh de bateria')
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        mensagem = "esse carro consegue percorrer aproximadamente " + str(range)
        mensagem += "Km com Carga total"
        print(mensagem)

#a classe carro
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
    def combustivel():
        print('o carro é movido a gasolina')

#a classe EletricCar que herda a classe carro
class EletricCar(Car):
    """cria um carro só que elétrico"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Battery()
    def combustivel(self):
        print('este carro é movido a energia elétrica, não precisa de gasolina.')

my_tesla = EletricCar('Tesla', 'Model S', '2016')

print(my_tesla.get_desc())


EletricCar.combustivel(my_tesla)
my_tesla.bateria.desc_bat()
my_tesla.bateria.get_range()