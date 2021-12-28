from random import randint
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Na nossa lista somando todos os numeros pares temos. {soma} ')


numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)
