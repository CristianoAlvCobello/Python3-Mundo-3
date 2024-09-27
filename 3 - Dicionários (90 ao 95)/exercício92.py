from datetime import date

dados = {}

dados['nome'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] =  (dados['idade']+(35 - (date.today().year - dados['contratação'])))
print('-='*50)
print(dados)
for chave, valor in dados.items():
    print(f'{chave} tem valor {valor}')
