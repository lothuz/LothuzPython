exp = str(input('Digite uma expressao: '))
pilha = []
for sim in exp:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('exp valida')
else:
    print('Exp invalida')
