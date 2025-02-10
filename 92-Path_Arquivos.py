#para localizar arquivos fora do diretório atual.
#utilize uma barra invertida "\"

with open('text_files\nome_do_arquivo.txt') as file_object:

#caso não funcione é possível utilizar paths absolutos
#como por exemplo:

with open('C:\Users\Dio\other_files\text_files\nome_do_arquivo.txt') as file_object: