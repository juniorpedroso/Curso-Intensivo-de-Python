hugo = {
    'nome': 'hugo', 'sobrenome': 'pedroso',
    'idade': '23', 'cidade': 'sorocaba',
}

igor = {
    'nome': 'igor', 'sobrenome': 'pedroso',
    'idade': '25', 'cidade': 'sorocaba',
}

neide = {
    'nome': 'neide', 'sobrenome': 'carniato',
    'idade': '73', 'cidade': 'taguai',
}

jose = {
    'nome': 'josé', 'sobrenome': 'de julio',
    'idade': '65', 'cidade': 'avaré',
}

pessoas = [hugo, igor, neide, jose]

for pessoa in pessoas:
    print('Nome: ' + pessoa['nome'].title() + 
    ' - ' + pessoa['sobrenome'].title())
    print('\tIdade: ' + pessoa['idade'] + 
    ' - ' + 'Cidade: ' + pessoa['cidade'].title())
    print()
