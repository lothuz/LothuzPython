jogador = {}
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
       partidas.append(int(input(f'Quantos gols foram feitos na {c + 1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador ['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        decisao = str(input('Deseja continuar? [S/N]')).upper()
        if decisao in 'SN':
            break
        print('ERRO Digite [S] ou [N] ')
    if decisao == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f' {k:>2}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Digite um codigo para busca: [999 finaliza o programa] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro não exise jogador com esse codigo {busca}. ')
    else:
        print(f'   Levantando dados do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'Na Partida {i+1} foram {g} Gols. ')
print('-='*30)
print('VOlte sempre.')