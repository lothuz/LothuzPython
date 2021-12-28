pal = str(input('Digite uma frase ou palavra: ')).strip().upper()
palavras = pal.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('A frase "{}" não é um palindromo'.format(pal))
