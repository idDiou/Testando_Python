#'open()' pode ser utilizado para abrir arquivos e 'close()' para fechar
#palavra reservada 'with' sendo utilizada no seguinte exemplo para que o programa feche sozinho.
#método 'read()' utilizado para ler o arquivo
with open ('pi.txt') as conteudo_arquivo:
    contents = conteudo_arquivo.read()
#ali conseguimos colocar até qual numero queremos que o programa leia
print(contents[:52])