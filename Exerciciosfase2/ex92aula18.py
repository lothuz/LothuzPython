from datetime import datetime
lista = {}
lista['nome'] = str(input('Digite o nome: '))
nasci = int(input('Digite ano de nascimento: '))
lista['idade'] = datetime.now().year - nasci
lista['carteira'] = int(input('Digite numero da CTPS: (0 zero não tem) '))
if lista['carteira'] != 0:
    lista['admissao'] = int(input('Admissão: '))
    lista['salario'] = float(input('Salário: '))
    lista['aposentadoria'] = lista['idade'] + ((lista['admissao'] + 35) - datetime.now().year)
print('-='*30)
for k,v in lista.items():
    print(f'{k}: {v}')


