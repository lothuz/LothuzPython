from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1)
    if p == 0:
        p = 1
        print('Contagem de 0 em 0 não existe, portanto foi substítuido por 1 em 1.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
            sleep(0.2)
    print()
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.2)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Escolha a forma que quer contar!!')
print('-='*30)
i1 = int(input('Inicio: '))
f1 = int(input('Final: '))
p1 = int(input('De quanto em quanto? '))
contador(i1, f1, p1)
print('FIMMMMMM')