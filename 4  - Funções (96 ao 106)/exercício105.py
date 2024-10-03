def notas(*notas, situacão=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    : nota: uma ou mais notas dos alunos (aceita várias)
    : situação: valor opcional, indicando se deve ou não adicionar a situação
    : return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = {}
    dicio['total'] = 0
    soma = 0
    for nota in notas:
        dicio['total'] += 1
        soma += nota
        if dicio['total'] == 1:
            dicio['maior'] = nota
            dicio['menor'] = nota
        else: 
            if dicio['maior'] < nota:
                dicio['maior'] = nota
            if dicio['menor'] > nota:
                dicio['menor'] = nota
    dicio['média'] = soma/dicio['total']
    if situacão == True:
        if dicio['média'] > 6:
            dicio['situação'] = 'BOA'
        else:
            dicio['situação'] = 'RUIM'
    return dicio

resposta = notas(5.5, 9.5, 10, 6.5, True)
print(f'\n{resposta}\n')
help(notas)
