pessoas = []
resposta = 's'
totalIdades = 0
mulheres = []

while resposta == 's':
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo(M/F): ')).lower()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    totalIdades += pessoa['idade']
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa['nome'])
    
    resposta = str(input('Quer continuar(S/N)? ')).lower()
    print('')

print(f'- O grupo tem {len(pessoas)}')
print(f'- A média de idade é de {totalIdades/len(pessoas)}')
print(f'- As mulheres cadastradas foram: {mulheres}')
print('- Lista de pessoas que estão acima da média:\n')

for individuo in pessoas:
    for chave, valor in individuo.items():
        if chave == 'idade' and valor > 26.75:
            print(individuo)
            print('')
            