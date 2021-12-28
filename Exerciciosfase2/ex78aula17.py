listanum = []
mai = 0
men = 0
for c in range (0, 5):
    listanum.append(int(input(f'Digite o numero na {c+1}ª posição: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('_'*30)
print(f'Os numeros digitados são {listanum}')
print(f'O maior numero é {mai} e está nas posições: ', end='')
for s,z in enumerate(listanum):
    if z == mai:
        print(f'{s+1}ª,',end='')
print()
print(f'O menor numero é {men} e está nas posições: ', end='')
for e,d in enumerate(listanum):
    if d == men:
        print(f'{e+1}ª,', end='')
