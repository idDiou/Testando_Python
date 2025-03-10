filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    msg = 'Desculpe, não encontramos o arquivo ' + filename
    print(msg)
