# Exercício 08 13
def build_profile(nome, sobrenome, **dados_gerais):
    profile = {}
    profile['nome'] = nome
    profile['sobrenome'] = sobrenome
    for key, value in dados_gerais.items():
        profile[key] = value
    return profile


user_profile = (build_profile('junior', 'pedroso',
                cidade = 'Avaré', idade = '50', filhos = '2'))

print()
for k, v in user_profile.items():
    print(f'{k}: {v}')
print()