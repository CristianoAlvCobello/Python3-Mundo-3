from math import sqrt

def calcularArea(altura, largura):
    area = altura**2*largura**2
    area = sqrt(area)
    print(f'A área de um terreno {largura:.1f}x{altura:.1f} é de {area:.1f}m²')

altura = float(input('Altura(m): '))
largura = float(input('Largura (m): '))

calcularArea(altura, largura)
