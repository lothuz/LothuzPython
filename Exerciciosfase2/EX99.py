from time import sleep
def maior(* num):
    cont = maior = 0
    print('=+' * 30)
    print('Analisando os Valores...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores. ')
    print(f'O maior valor foi {maior}. ')




maior(4, 2, 5, 6, 9, 10)
maior(1,2)
maior(9, 5, 3, 6, 1)
maior(0)