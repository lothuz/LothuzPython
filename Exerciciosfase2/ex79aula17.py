numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado, não adicionado.')
    r = str(input('Gostaria de continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'A sua lista ficou assim: {numeros}')