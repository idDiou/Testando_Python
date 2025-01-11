#para o exercicio 80

def impress (unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('printing model: ' + current_design)
        completed_models.append(current_design)

def show_impress(completed_models):
    print('\nos modelos finalizados:')
    for completed_model in completed_models:
        print(completed_model)

