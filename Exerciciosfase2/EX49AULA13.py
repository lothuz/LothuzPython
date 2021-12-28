num = int(input('Digite um numero para taboada até o 10: '))
for c in range (1, 11):
    print('{} X {} = {}'.format(num, c, num*c))