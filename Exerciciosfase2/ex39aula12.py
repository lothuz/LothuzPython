from datetime import date
atual = date.today().year
nasci = int(input('Digite seu ano de nascimento: '))
idade = atual - nasci
if idade == 18:
    print('Esta na hora de se alistar!!')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} ano(S) para seu alistamento!'.format(saldo))
else:
    saldo = idade - 18
    print('Já se passou {} ano(S) do seu alistamento, se não se alistou, já passou da hora.'.format(saldo))