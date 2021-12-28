la = float(input('Digite um lado: '))
lb = float(input('Digite outro lado: '))
lc = float(input('Digite outro lado: '))
if la == lb and la == lc:
    print('ESSE TRIANGULO É EQUILATERO')
elif la == lb or lb == lc or la == lc:
    print(' Triangulo isosceles')
else:
    print('Triangulo escaleno')

