numero = int(input('Escolha um numero: '))
print ('''para converter esse nunero, escolha uma das seguintes opçoes:
1 - binario
2 - octal
3 - hexadecimal ''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O numero {}, convertido em binário fica {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O numero {}, convertido em octal fica {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O numero {}, convertido em hexadecimal {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida.')