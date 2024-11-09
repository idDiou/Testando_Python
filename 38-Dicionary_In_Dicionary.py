#é possível aninhar informações, dicionários dentro de dicionários.
usuarios = {'dio':{'first':'Dionata', 'last':'Borges', 'moradia': 'Cachoeirinha'}, 'Katoryn':{'first':'Katlyn', 'last':'Resmin', 'moradia': 'Cachoeirinha'}}


for username, user_info in usuarios.items():
    print("Username: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['moradia']
    print('nome completo: ' + full_name.title())
    print('mora em: ' + location)