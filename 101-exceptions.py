#tratando erros com python

try:
    print(5/0)
except ZeroDivisionError:
    print('você não pode dividir por zero')