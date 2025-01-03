#essa é a versão sem função
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
modelos_completos = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print('printing model: ' + current_design)
    modelos_completos.append(current_design)
    
print('\nos modelos finalizados:')

for completed_model in modelos_completos:
    print(completed_model)