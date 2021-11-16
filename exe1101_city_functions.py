def nome_cidade_pais(cidade, pais):
    """[Junta o nome de uma cidade e o de um país de forma elegante]

    Args:
        cidade ([type]): [description]
        pais ([type]): [description]

    Returns:
        [type]: [description]
    """
    cidade_pais = f'{cidade.title()}, {pais.title()}'
    return cidade_pais
