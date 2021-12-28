peso = float(input('Digite seu peso: ' ))
altura = float(input('Digite sua altura: '))
imc = peso / ( altura * 2 )
if imc < 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso!'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.2f}, vocÊ está no peso ideal!'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.2f}, você esta no SOBREPESO!'.format(imc))
elif imc <=40:
    print(' IMC {:.2f}, OBESIDADE'.format(imc))
else:
    print(' IMC {:.2f} OBeSiDADE MORBIDA'.format(imc))