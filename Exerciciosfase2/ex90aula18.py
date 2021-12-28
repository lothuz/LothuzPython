aluno = {}
while True:
    aluno['nome'] = str(input('Digite o nome: '))
    aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        print(f'O aluno {aluno["nome"]}, foi aprovado! ')
    elif aluno['media'] <= 5:
        print(f'O aluno {aluno["nome"]} foi reprovado!')
    else:
        print(f'O aluno {aluno["nome"]} está de recuperação!')
    decisao = str(input('Gostaria de continuar? [S/N] '))
    if decisao in 'Nn':
        break
print('Volte sempre!!')