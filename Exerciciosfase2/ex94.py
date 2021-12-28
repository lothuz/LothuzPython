dados = {}
lista = list()
soma = media = 0
mulheres = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if dados['sexo'] not in 'MmFf':
        print('erro, sexo errado digite novamente os dados')
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Digite sua idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    decisao = str(input('Gostaria de continuar? [S/N]'))
    if decisao not in 'SsNn':
        print('dados errados, digite novamente: ')
        decisao = str(input('Gostaria de continuar? [S/N]'))
    if decisao in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas. ')
print('-=' * 30)
media = soma / len(lista)
print(f'A média de idade é {media:5.2f} anos.' )
print('-=' * 30)
print(f'As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}, ')
print('-=' * 30)
print(f'As pessoas com idade acima da media são: ', end='')
for d in lista:
    if d['idade'] > media:
        print(f'{d["nome"]}, tem {d["idade"]} anos, sexo {d["sexo"]}')
print('Encerrando...')