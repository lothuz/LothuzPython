dados = []
dados2 = []
mai = men = 0
while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(dados2) == 0:
        mai = men = dados[1]
    elif dados[1] >= mai:
        mai = dados[1]
    elif dados [1] <= men:
        men = dados[1]
    dados2.append(dados[:])
    dados.clear()
    decisao = str(input('Gostaria de continuar? [S/N] '))
    if decisao in 'Nn':
        break
print ('-='*30)
print(f'Foram cadastrado {len(dados2)} Pessoas. ')
print(f'O menor peso foi de {men}Kg de ', end='')
for c in dados2:
    if c[1] == men:
        print(f'{c[0]},')
print(f'O maior peso foi de {mai}Kg de ', end='')
for b in dados2:
    if b[1] == mai:
        print(f'{b[0]},')