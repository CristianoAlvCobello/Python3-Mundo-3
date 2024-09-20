contador = 0 
pessoa = list()
galera = list()
pessoasLeves = list()
pessoasPesadas = list()

while True:
    contador += 1
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()

    for peso in galera:
        if contador == 1:
            maior = peso[1]
            menor = peso[1]
        else:
            if maior < peso[1]:
                maior = peso[1]

            elif menor > peso[1]:
                menor = peso[1]


    mais = str(input('Quer mais(s/n)? ')).lower()
    if mais != 's':
        break

for leveEpesados in galera:
    if maior == leveEpesados[1]:
        pessoasPesadas.append(leveEpesados[0])
    elif menor == leveEpesados[1]:
        pessoasLeves.append(leveEpesados[0])

print(f'\nForam {contador} pessoas cadastradas')
print(f'O Maior peso foi {maior}Kg, das seguintes pessoas: {pessoasPesadas}')
print(f'O Menor peso foi {menor}Kg, das seguintes pessoas: {pessoasLeves}')
