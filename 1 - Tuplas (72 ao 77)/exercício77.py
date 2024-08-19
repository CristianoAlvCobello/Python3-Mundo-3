palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for vogais in palavras: 
    if 'a' in vogais or 'e' in vogais or 'i' in vogais or 'o' in vogais or 'u' in vogais:
        print(f'Na palavra {vogais.upper()} temos {'a '*vogais.count('a')}{'e '*vogais.count('e')}{'i '*vogais.count('i')}{'o '*vogais.count('o')}{'u '*vogais.count('u')}')
    else:
        print(f'Na palavra {vogais.upper()} não temos')
