
#bateria para o exercicio 87, da subclasse de carro, o carro elétrico
class Battery():
    """uma tentativa simples de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def desc_bat(self):
        print('este carro tem ' + str(self.battery_size)+'-kWh de bateria')