#inicia na pagina 199

#é necessário o "__init__"

#classes sempre começam com letra maiuscula por convenção.
class Dog():
    """modelando um cachorro"""
    def __init__(self, name, age):
        """"inicializa os atributos"""
        self.name = name
        self.age = age
    def sentar(self):
        """simula um cachorro sentando em resposta a um comando"""
        print('**comando sentar**')
        print(self.name.title()+ ' agora sentou.')
    def rolar(self):
        """simula um cachorro rolando em resposta a um comando"""
        print('**comando rolar**')
        print(self.name.title() + ' rolou.')

my_dog = Dog('Willie', 6)

#frequentemente python utiliza a notação de ponto para encontrar o caminho das coisas, como no exemplo a seguir:

print('o nome do meu cachorro é ' +my_dog.name.title() +'.')

#utilizando o método str converte o valor do atributo age em uma string.
print('e ele tem ' + str(my_dog.age)+' anos.')

#chamando os métodos da classe Dog através da variavel my_dog junto da notação de ponto e o nome especifico do método.
my_dog.sentar()
my_dog.rolar()

your_dog = Dog('Lucinda', 4)

print('\nseu cachorro se chama '+your_dog.name.title()+' certo?')
print('deve ter cerca de ' + str(your_dog.age)+' anos.')

your_dog.sentar()