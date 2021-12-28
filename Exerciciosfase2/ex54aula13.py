from datetime import date
ano = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - nascimento < 18:
        cont += 1
    elif ano - nascimento >= 18:
        cont2 += 1
print('Existem {} pessoa(s) menor de 18 anos e {} pessoa(s) maior de 18 anos'.format(cont, cont2))
