numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))

while numero > 20 or numero < 0:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
else:
    print(f'\nVocê digitou o número\033[32;1m {numeros[numero]}\033[m')
