#para evitar que a função leve embora os itens de uma lista e deixe ela vazia

#código do exemplo anterior para teste
def impress (unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('printing model: ' + current_design)
        modelos_completos.append(current_design)

def show_impress(completed_models):
    print('\nos modelos finalizados:')
    for completed_model in modelos_completos:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
modelos_completos = []


#nome_da_função(nome_da_lista[:])  <--a notação de fatia [:] cria uma cópia da lista para ser enviada para a função
impress(unprinted_designs[:], modelos_completos)
show_impress(modelos_completos)

print(unprinted_designs)