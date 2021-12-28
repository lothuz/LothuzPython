from random import randint
from time import sleep
jogos = []
lista = []
print('_=     Jogos da Mega Sena    =_')
quant = int(input('Quantos jogos você vai querer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' Sorteando {quant} jogos ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} :{l}')
    sleep(1)