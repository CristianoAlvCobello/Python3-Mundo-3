expressao = str(input('Digite uma expressão: '))

if expressao[0] == '(':
    if expressao.count('(') != expressao.count(')'):
        print('Expressão inválida')
    else:
        print('Expressão válida')
else:
    print('Expressão inexistente')

#Resposta do professor

#expressao = str(input('Digite a expressão: '))
#pilha = []
#for simbolo in expressao:
#    if simbolo : pilha.append('(')
#    elif simbolo == ')':
#       if len(pilha) > 0: 
#           pilha.pop()
#    else: 
#       pilha.append(')')
#       break
#if len(pilha) == 0: 
#    print('Sua expressão está válida!')
#else: 
#    print('Sua expressão está errada')