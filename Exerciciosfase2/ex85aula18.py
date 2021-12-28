lista = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
print(f'pares {lista[0]}')
lista[1].sort()
print(f'impares {lista[1]}')