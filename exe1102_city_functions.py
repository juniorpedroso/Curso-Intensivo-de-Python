def nome_cidade_pais(cidade, pais, populacao=''):
    """[Junta o nome de uma cidade e o de um país de forma elegante]
    """
    if populacao:
        cidade_pais = f'{cidade.title()}, {pais.title()} - população {populacao}'
    else:
        cidade_pais = f'{cidade.title()}, {pais.title()}'
    return cidade_pais
