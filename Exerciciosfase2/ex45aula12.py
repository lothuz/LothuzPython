from random import randint
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Escolha uma das opções para
[0] pedra
[1] papel
[2] tesoura: '''))
print('Computador jogou {}'.format(lista[computador]))
print('jogador jogoU {}'.format(lista[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    if jogador == 1:
        print('JOOGADOR VENCEU!')
    if jogador == 2:
        print('COMPUTADOR VENCEU!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR VENCEU!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    if jogador == 1:
        print('COMPUTADOR VENCEU!')
    if jogador == 2:
        print('EMPATE')
else:
    print('ERRO JOGADA INVALIDA!')