
#bateria para o exercicio 87, da subclasse de carro, o carro elétrico
class Battery():
    """uma tentativa simples de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def desc_bat(self):
        print('este carro tem ' + str(self.battery_size)+'-kWh de bateria')
    def get_range(self):
        range = self.battery_size * 3
        mensagem = "esse carro consegue percorrer aproximadamente " + str(range)
        mensagem += "Km com Carga total"
        print(mensagem)
    def upgrade_bat(self, num = 80):
        self.num = num
        if self.num > self.battery_size:
            print('carregando o carro até ' + str(self.num) + '%')
            self.battery_size = self.num