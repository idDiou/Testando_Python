from carro_eletrico import EletricCar

tesla = EletricCar('Tesla', 'G5', '2025')

tesla.bateria.desc_bat()
tesla.bateria.get_range()

tesla.bateria.upgrade_bat(90)
tesla.bateria.desc_bat()
tesla.bateria.get_range()