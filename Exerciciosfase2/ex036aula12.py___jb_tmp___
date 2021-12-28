'''ESCREVA UM PROGRAMA QUE APROVE UM EMPRESTIMO IMOBILIARIO. O PROGRAMA DEVE PERGUNTAR O VALOR DA CASA,
SALARIO DO CLIENTE E EM QUANTOS ANOS ELE VAI PAGAR. CALCULAR O VALOR QUE ELE VAI PAGAR mensal, NAO PODENDO
EXCEDER EM 30% O SALARIO DO CLIENTE , SENAO SERA RECUSADO.'''

valor_casa = float(input('Digite o valor do crédito em reais: '))
salario = float(input('Digite seu salario BRUTO: '))
anos = int(input('Digite em quantos anos você vai pagar: '))
juros = valor_casa * 0.0055
valor_mensal = (( valor_casa / anos ) / 12) + juros
meses = anos * 12
salario_div = salario * 0.30
if salario_div < valor_mensal:
    print('O seu crédito foi recusado, pois você nao comporta a parcela, talves em um prazo maior, conseguimos aprovar!.')
else:
    print('O valor mensal do seu imovel fica em R${:.2f} pagos em {} meses.'.format(valor_mensal, meses))