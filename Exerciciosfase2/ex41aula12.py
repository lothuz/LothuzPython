'''xercício Python 041: A Confederação Nacional de Natação precisa
de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''



from datetime import date
ano = date.today().year
nasci = int(input('Digite o ano de nascimento '))
idade = ano - nasci
if idade <= 9:
    print('você possui {} ano(s), sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print(' Você possui {} ano(s), sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você possui {} ano(s), sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('Voce possio {} ano(s), sua categoria é SÊNIOR'.format(idade))
else:
    print('Voce possui {} ano(s), sua categoria é MASTER'.format(idade))