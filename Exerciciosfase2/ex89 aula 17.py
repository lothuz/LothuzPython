ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    decisao = str(input('Gostaria de continuar? [S/N]'))
    if decisao in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome ":<10}{"Media":>8}')
print('-='*26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*30)
    opc = int(input('Gostaria de mostrar as notas de qual aluno? [999 interrompe] '))
    if opc == 999:
        break
        print('Finalizando....')
    if opc <= len(ficha):
        print(f' As notas de {ficha[opc][0]}, ficaram {ficha[opc][1]} ')
print('volte sempre! ')