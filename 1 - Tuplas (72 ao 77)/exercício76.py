produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
nome = 0
preco = 1

print('='*40)
for listagem in produtos:
    if len(produtos) > nome:
        print(f'{produtos[nome]}', '.'*(30-len(produtos[nome])), end='')
        print(f'R$ {produtos[preco]:>6}')
        nome += 2
        preco += 2
print('='*40)
