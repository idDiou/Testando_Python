#algoritmo que retorne quantos numeros primos tem em um determinado intervalo de valores

#só deve ser divisivel por 1 e por si próprio
#2 é o unico numero par primo

class TestadorDePrimos:
    def __init__(self):
        self.lista_primos = []
    def iniciando(self):
        valore = input('digite seu intervalo\n')
        listown = list(range(1, int(valore)))
        for valo in listown:
            print(valo)
            self.testando_p(int(valo))
        self.resultado(int(valore))
    def testando_p(self, valor):
        valor = valor
        aumento = True
        tester = 1
        while aumento:
            tester += 1
            if valor == 1:
                break
            if tester < int(valor):
                if int(valor) % 2 == 0:
                    print(str(valor) + ' é par, não é primo')
                    break
                if int(valor) % tester == 0:
                    resultado = int(valor) % tester
                    print(str(valor) + ' dividido por ' + str(tester) + ' sobra ' + str(resultado) + ' não é primo.')
                    break
            if tester == valor:
                print(str(valor) + ' é primo')
                self.lista_primos.append(valor)
                aumento = False
    def resultado(self, limite):
        contagem = len(self.lista_primos)
        print('dentro do numero ' + str(limite) + ' temos um total de ' + str(contagem) + ' numeros primos: ' + str(self.lista_primos))

# Criando a instância da classe e iniciando o processo
testador = TestadorDePrimos()
testador.iniciando()