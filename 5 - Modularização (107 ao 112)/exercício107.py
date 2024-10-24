from UtilidadesCeV import moeda

valor = float(input('Digite o valor: R$'))
print(f'\nA metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(valor, 13)}')
