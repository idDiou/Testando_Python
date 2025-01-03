#par de asteriscos faz python criar um dicionários vazio
def construindo_usuario(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

#se atentar ao chamado da função "return", ao ser chamada dentro de um laço for ela o encerra.

user_profile = construindo_usuario ('albert', 'einstein', location ='princeton', estudo = 'Fisica', cabelo = 'branco')
print(user_profile)
