valor = float(input('Informe o valor do Produto: '))
forma = str(input('Informe o meio de pagamento digitando 1 para vista ou 2 a prazo: '))
if forma == '1':
    paga = str(input('Informe como quer pagar, 1 cartão, 2 cheque ou dinheiro: '))
    if paga == '1':
        print('O valor a ser pago é R${:.2f}, com desconto de 5%.'.format(valor * 0.95))
    elif paga == '2':
        print('O valor a ser pago é R${:.2f}, com desconto de 10%.'.format(valor * 0.90))
    else:
        print('ERRO INFORME O NUMERO CORRETO')
elif forma == '2':
    vezes = int(input('Informe a quantidade de vezes : '))
    if vezes == 2:
        print('O valor a ser pago será de 2x de R${:.2f}, sem desconto'.format(valor / 2))
    elif vezes >= 3:
        print('O valor a ser pago será de {}x de R${:.2f}, com 20% de juros'.format(vezes, (valor * 1.20) / vezes ) )
    else:
        print('ERRO, INFORME QUANTIDADE DE VEZES CORRETA')
else:
    print('ERRO , INFORME A OPÇÃO CORRETA!')

